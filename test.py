import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.datasets import mnist
from keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Load MNIST test dataset
(_, _), (x_test, y_test) = mnist.load_data()

# Preprocess test data
x_test = np.expand_dims(x_test, axis=-1)
x_test = x_test.astype('float32') / 255.0
y_test_cat = to_categorical(y_test, num_classes=10)

# Load the trained model
model = load_model("handwritten.h5")

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test_cat, verbose=0)
print('Test Accuracy: {:.2f}%'.format(accuracy * 100))

# Predict classes
y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred_classes)

# Plot the confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Optional: display a few test images with predictions
for i in range(5):
    plt.imshow(x_test[i].reshape(28,28), cmap='gray')
    plt.title(f"True: {y_test[i]}, Predicted: {y_pred_classes[i]}")
    plt.show()
