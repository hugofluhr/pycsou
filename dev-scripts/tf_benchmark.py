import tensorflow as tf
from tqdm import tqdm


def foo(x, y):
    z = x * y
    return z


if __name__ == "__main__":
	with tf.device("/CPU:0"):
		z0 = None
		x = tf.random.uniform((1024 * 12, 1024 * 12), dtype=tf.float32)
		y = tf.random.uniform((1024 * 12, 1024 * 12), dtype=tf.float32)
		for _ in tqdm(range(5000)):
			zz = foo(x, y)
			if z0 is None:
				z0 = zz
			else:
				z0 += zz
