import numpy as np

from tatau.nn.tatau.summarizer import Summarizer


class Mean(Summarizer):
    """
    Mean Weights Summarizer

    """

    def summarize(self, updates):
        new_weights = list()
        for weights_list_tuple in zip(*updates):
            new_weights.append(
                [
                    np.mean(np.array(weights_), axis=0, dtype=self.dtype)
                    for weights_ in zip(*weights_list_tuple)
                ]
            )
        return new_weights
