from metrics.bleu import compute_bleu

def compute_metrics(references,generated) -> dict:
    """
    Calculates various metrics and returns the calculated dict of these matrics.
    args:
        reference: list of lists of references for each translation. Each
          reference should be tokenized into a list of tokens.
        translation: list of translations to score. Each translation
          should be tokenized into a list of tokens.
    returns:
        A dicitonary with different metrics intact.
    """
    metrics_dict = {} #Update as in new metrics are added over here.
    metrics_dict["smoothed_bleu"] = compute_bleu(references,generated,smooth=True)
    metrics_dict["bleu"] = compute_bleu(references,generated,smooth=False)
    
    return metrics_dict