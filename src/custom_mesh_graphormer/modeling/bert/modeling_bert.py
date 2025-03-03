from transformers.models.bert.modeling_bert import *

for symbol in dir(modeling_bert):
    if not symbol.startswith("_"):
        globals()[symbol] = getattr(modeling_bert, symbol)
