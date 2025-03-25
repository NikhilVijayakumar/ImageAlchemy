import cv2
import numpy as np
import matplotlib.pyplot as plt


class BasicImageOperations:
    def __init__(self, img1=None, img2=None):
        self.img1 = img1
        self.img2 = img2

    def load_image(self, path):
        """Loads an image from the specified path."""
        return cv2.imread(path)

    def set_img1(self, img):
        """Sets img1 to the provided image."""
        if isinstance(img, str):
            self.img1 = self.load_image(img)
        else:
            self.img1 = img

    def set_img2(self, img):
        """Sets img2 to the provided image."""
        if isinstance(img, str):
            self.img2 = self.load_image(img)
        else:
            self.img2 = img

    def add_images(self):
        """Adds two images pixel-wise."""
        if self.img1 is None or self.img2 is None:
            raise ValueError("Both images must be loaded first.")
        return cv2.add(self.img1, self.img2)

    def subtract_images(self):
        """Subtracts img2 from img1 pixel-wise."""
        if self.img1 is None or self.img2 is None:
            raise ValueError("Both images must be loaded first.")
        return cv2.subtract(self.img1, self.img2)

    def multiply_images(self):
        """Multiplies two images pixel-wise."""
        if self.img1 is None or self.img2 is None:
            raise ValueError("Both images must be loaded first.")
        return cv2.multiply(self.img1, self.img2)

    def divide_images(self):
        """Divides img1 by img2 pixel-wise, avoiding division by zero."""
        if self.img1 is None or self.img2 is None:
            raise ValueError("Both images must be loaded first.")
        return cv2.divide(self.img1, self.img2 + 1)

    def apply_logarithmic_transform(self, img=None):
        """Applies a logarithmic transform to the image."""
        if img is None:
            if self.img1 is None:
                raise ValueError("An image must be loaded first.")
            img = self.img1
        img_float = img.astype(np.float32)
        result = np.log(img_float + 1)
        result = (result - np.min(result)) / (np.max(result) - np.min(result)) * 255
        return result.astype(np.uint8)

    def apply_exponential_transform(self, img=None):
        """Applies an exponential transform to the image."""
        if img is None:
            if self.img1 is None:
                raise ValueError("An image must be loaded first.")
            img = self.img1
        img_float = img.astype(np.float32)
        result = np.exp(img_float / 255.0)
        result = (result - np.min(result)) / (np.max(result) - np.min(result)) * 255
        return result.astype(np.uint8)

    def apply_square_root_transform(self, img=None):
        """Applies a square root transform to the image."""
        if img is None:
            if self.img1 is None:
                raise ValueError("An image must be loaded first.")
            img = self.img1
        img_float = img.astype(np.float32)
        result = np.sqrt(img_float)
        result = (result - np.min(result)) / (np.max(result) - np.min(result)) * 255
        return result.astype(np.uint8)

    def invert_image(self, img=None):
        """Inverts the image."""
        if img is None:
            if self.img1 is None:
                raise ValueError("An image must be loaded first.")
            img = self.img1
        return cv2.bitwise_not(img)

    def display_result(self, result, title, output_dir=None):
        """Displays a single image with its title and optionally saves it to a directory."""
        plt.figure(figsize=(6, 6))
        if len(result.shape) == 3:
            plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        else:
            plt.imshow(result, cmap='gray')
        plt.title(title)
        plt.axis('off')  # Turn off axis for cleaner display
        plt.tight_layout()

        if output_dir:
            import os
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            plt.savefig(os.path.join(output_dir, f'{title}.png'))

        try:
            plt.show()
        except Exception as e:
            print(f"Failed to display plot: {e}")
            print("Consider saving the plot to a file instead.")

        # Clear the figure for the next plot
        plt.clf()


# Example usage
if __name__ == "__main__":
    operations = BasicImageOperations()
    output_dir = "/home/dell/PycharmProjects/ImageAlchemy/output"

    # Set images using paths
    operations.set_img2('/home/dell/PycharmProjects/ImageAlchemy/test_images/house.tif')
    operations.set_img1('/home/dell/PycharmProjects/ImageAlchemy/test_images/cameraman.tif')

    result_add = operations.add_images()
    operations.display_result(result_add, 'Addition',output_dir)

    result_subtract = operations.subtract_images()
    operations.display_result(result_subtract, 'Subtraction',output_dir)

    result_multiply = operations.multiply_images()
    operations.display_result(result_multiply, 'Multiplication',output_dir)

    result_divide = operations.divide_images()
    operations.display_result(result_divide, 'Division',output_dir)

    result_log = operations.apply_logarithmic_transform()
    operations.display_result(result_log, 'Logarithmic',output_dir)

    result_exp = operations.apply_exponential_transform()
    operations.display_result(result_exp, 'Exponential',output_dir)

    result_sqrt = operations.apply_square_root_transform()
    operations.display_result(result_sqrt, 'Square Root',output_dir)

    result_invert = operations.invert_image()
    operations.display_result(result_invert, 'Invert',output_dir)

