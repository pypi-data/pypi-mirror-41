### transformer的keras实现
#### 层
  所有在transformer中用到的层都在layers.py中实现,目前实现了
  `SelfAttention,MultiHeadAttention,MaskLayer`,都是keras的自定义层
  
  `transformer_block`也可以当做层使用, 是原论文中encoder一个block的实现
  

#### 预训练任务
   输入带[mask]的句子,输出[mask]的
   

