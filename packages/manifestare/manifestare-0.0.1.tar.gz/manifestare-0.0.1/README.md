# manifestare

A _manifesto_ is a textual genre that consists of a kind of formal, persuasive and public statement for the transmission of opinions, decisions, intentions and ideas. **We want it for data**!

This library intend to provide a simple, fluent, and descriptive API to explicit DataFrames expectations. It supports both `pyspark.DataFrame` and `pandas.DataFrame`.

---

## Features
### `PandasDataFrameManifesto`
##### `__init__()`

Creates a `PandasDataFrameManifesto` instance to explicit define expectations about a given `pandas.Dataframe`.

```python
from manifestare.core import PandasDataFrameManifesto

manifesto = PandasDataFrameManifesto()

assert isinstance(manifesto, PandasDataFrameManifesto) 
```

##### `describeThat(df)`

Set a DataFrame in the Manifesto to be evaluated against matchers. 

```python
import pandas as pd
from manifestare.core import PandasDataFrameManifesto

data = {
    'x': [0, 1],
    'y': [1, 0]
}

df = pd.DataFrame(data)

manifesto = PandasDataFrameManifesto()
manifesto.describeThat(df)

assert manifesto.df != None 
```

##### `doesHaveColumn(column)`

Evaluate if a given column exists in the DataFrame being described.

```python
import pandas as pd
from manifestare.core import PandasDataFrameManifesto

data = {
    'x': [0, 1],
    'y': [1, 0]
}

df = pd.DataFrame(data)

# pass
PandasDataFrameManifesto()\
    .describeThat(df)\
    .doesHaveColumn('x')
    
# fail
PandasDataFrameManifesto()\
    .describeThat(df)\
    .doesHaveColumn('z')
```

---

### `SparkDataFrameManifesto`
##### `__init__()`

Creates a `SparkDataFrameManifesto` instance to explicit define expectations about a given `pyspark.sql.Dataframe`.

```python
from manifestare.core import SparkDataFrameManifesto

manifesto = SparkDataFrameManifesto()

assert isinstance(manifesto, SparkDataFrameManifesto) 
```

##### `describeThat(df)`
Set a DataFrame in the Manifesto to be evaluated against matchers. 

```python
from pyspark.sql import SparkSession
from manifestare.core import SparkDataFrameManifesto

values, columns = [[(0, 1), (1, 0)], ['x', 'y']]

spark = SparkSession.builder.appName('manifestare').getOrCreate()
df = spark.createDataFrame(values, columns)

manifesto = SparkDataFrameManifesto()
manifesto.describeThat(df)

assert manifesto.df != None 
```

##### `doesHaveColumn(column)`
Evaluate if a given column exists in the DataFrame being described.

```python
from pyspark.sql import SparkSession
from manifestare.core import SparkDataFrameManifesto

values, columns = [[(0, 1), (1, 0)], ['x', 'y']]

spark = SparkSession.builder.appName('manifestare').getOrCreate()
df = spark.createDataFrame(values, columns)

# pass
SparkDataFrameManifesto()\
    .describeThat(df)\
    .doesHaveColumn('x')

# fail
SparkDataFrameManifesto()\
    .describeThat(df)\
    .doesHaveColumn('z') 
```
