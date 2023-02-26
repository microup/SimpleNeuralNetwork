import time
from utils import get_success_rate
from config import  InputData, TargetData, filename, epochValue, percentStopTrain

def Train(model, TrainData, TrainTarget, epochValue, filename):
    model.compile(optimizer='adam', loss='mse')

    class CustomCallback(tf.keras.callbacks.Callback):
        def on_train_begin(self, logs=None):
            setattr(self, 'start_time', time.time())

        def on_epoch_end(self, epoch, logs={}):
            if epoch % 1000 == 0:
                success_rate = get_success_rate(model, InputData, TargetData)
                now = time.time()
                time_diff = now - \
                    getattr(self, 'last_log_time', self.start_time)
                total_time = now - getattr(self, 'start_time', now)
                print(
                    f"Epoch {epoch}: loss - {logs['loss']:.2f}, "
                    f"success rate: {success_rate:.2f}%, "
                    f"time between epochs: {time_diff:.2f} seconds, "
                    f"total time elapsed: {total_time:.2f} seconds")
                setattr(self, 'last_log_time', now)
                if success_rate >= percentStopTrain:
                    setattr(self.model, 'stop_training', True)

    model.fit(TrainData, TrainTarget, epochs=epochValue, verbose=0,
              callbacks=[CustomCallback()])
    model.save(filename)
    