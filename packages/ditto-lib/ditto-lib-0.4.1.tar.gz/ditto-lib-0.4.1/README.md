[![GitHub version](https://badge.fury.io/gh/hgromer%2Fditto.svg)](https://badge.fury.io/gh/hgromer%2Fditto)
[![PyPI version](https://badge.fury.io/py/ditto-lib.svg)](https://badge.fury.io/py/ditto-lib)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# Ditto: A data analysis library

**Ditto** is a data analysis library meant to make processing and accumulating data easier. It provides an easy to use API that is intuitive and allows the user to be more productive. **Ditto** utilizes different **Collections** to store data. These **Collections** are made of **Items**, and each **Item** is represented by various different **Attributes**. These **Collections** can be generated manually, or imported from various sources, such as csv files. An **Item** array that stores values called **Attributes**. Accessing, and modifying **Items** within these **Collections** is very user friendly.  

# Basic Usage

Assume we have the following csv file 'people.csv':

| Name | Weight | Age | 
| :-: | :-: | :-: |
| Jim | 160 | 20 | 
| Sally | 130 | 21 |
| Bob | 120 | 10 |
| Bill | 200 | 45 |
| Jen | 150 | 23 |

Below is an example of how to import the csv file into an **ItemCollection**:

```python

# Create the Item Collection by giving it a name
item_collection = ItemCollection('People')
# Import the csv file, giving a start_row and start_column to start at
item_collection.from_csv('people.csv', start_row=1, start_column=1)
```

The **from_csv** method assumes that the names of the items belonging to this **Collection** are located at start_column 0, and start at start_row **start_row**. All the start_columns from **start_column**, and onward are the attributes that will then be associated with the **Item** in that start_row. You can also use a string name to give the starting start_column, as shown below:

```python
item_collection.from_csv('people.csv', start_row=1, start_column='Weight')
```

Now that we are correctly storing our items within the **Collection**, we can access individual **Items** by name. We can also access each **Item's attributes** by name as well once the **Item** has been retrieved. Below is an example of how to retrieve the **Item** 'Bill', print all of it's **Attributes** and print the **Attribute** 'Weight':

```python
# Get the item
attributes = item_collection.get_item('Bill')
print(attributes)
>>> [200, 45]
# Print the attribute Weight
print(item_collection.get_item_attribute('Bill', 'Weight'))
>>> 200
```

In order to mantain consitency, all **Items** that belong to the same **Collection** must share the same set of **Attributes**. Additionally, **Items** store **Attributes** in the same order for every **Item** in a **Collection**. **Items** can have None type values associated with the **Attribute**, but it important to mantain the integrity of the **Collection** in this manner. In order to do this, when modifying **Items**, it is important to do so through the **Collection** API. Below is an example of how to add an attribute to an item:

```python
people.set_item_attribute('Bob', 3.5, 'GPA')
```

The **set_item_attribute** method will assign that **Attribute** to the **Item** given if it exists, if not it will create the **Attribute**, assign it to the **Item**, and update the entire **Collection**. Now, the **ItemCollection** will resemble the following:

| Name | Weight  |  Age | GPA |
| :-----: | :-: | :-: | :-: |
| Jim | 160 | 20 | |
| Sally | 130 | 21 | |
| Bob | 120 | 10 | |
| Bill | 200 | 45 | 3.5 |
| Jen | 150 | 23 | |

There are also some utilities that we can use in order to make analyzing information easier. We can merge and intersect **Collections**, as well as strip them to remove any noisy **Attributes**. Noisy **Attributes** are ones that contain the same value for every **Item** in a **Collection**. Assume we have another csv file called 'people2.csv':

| Name | Weight  |  Age | GPA |
| :-----: | :-: | :-: | :-: |
| Jim | 160 | 20 | 3.5 |
| Sally | 130 | 21 | 3.5 |
| Bob | 120 | 10 | 3.5 |
| Jen | 150 | 23 | 3.5 |
| Ashley | 200 | 24 | 3.5 |

 Below is an example of how to merge two **Collections**

```python
# Assume we have two Item Collection objects item_collection, to_merge
merged_collection = people.merge_collections(people2, 'Merged Collection')
```

As a result, the merged_collection will look like the following:

| Name | Weight  |  Age | GPA |
| :-----: | :-: | :-: | :-: |
| Jim | 160 | 20 | 3.5 |
| Sally | 130 | 21 | 3.5 |
| Bob | 120 | 10 | 3.5 |
| Bill | 200 | 45 | 3.5 |
| Jen | 150 | 23 | 3.5 |
| Ashley | 200 | 24 | 3.5 |

When merging **Collections**, if any **Items** are shared, they will combine their **Attributes**. Now let's remove any noise from the **Collection** by deleting any **Attributes** that share the same value for all **Items**

```python
merged_collection.strip()
```

Results in:

| Name | Weight  |  Age |
| :-----: | :-: | :-: |
| Jim | 160 | 20 |
| Sally | 130 | 21 |
| Bob | 120 | 10 |
| Bill | 200 | 45 |
| Jen | 150 | 23 |
| Ashley | 200 | 24 |

Instead of merging, you can also intersect **Collections**, which will create a new **Collection** that contains only **Items** that are found in both **Collections**. Again, any discrepancies between **Item Attributes** will be resolved by merging same item attributes. An example of an intersection is shown below:

```python
# Assume we have two Item Collection object item_collection, to_intersect
intersected_collection = people.intersect(people2, 'Intersected Collection')
```

As a result the intersected_collection will look like the following:

| Name | Weight  |  Age | GPA |
| :-----: | :-: | :-: | :-: |
| Jim | 160 | 20 | 3.5 |
| Sally | 130 | 21 | 3.5 |
| Bob | 120 | 10 | 3.5 |
| Jen | 150 | 23 | 3.5 |

# Attribute Usage
The **Attribute** is a class that contains a name and boolean value is_descriptor. If an **Attribute** is defined as being a descriptor, then it will be used when running the **Item** it belongs to through certain algorithms, such as a clustering algorithm. This distinction was made for the User's convenience, and all **Attributes** will default to being a descriptor.

- **copy**: Returns a deep copy of the attribute

# Item Usage
The **Item** isn't a literal class in order to mantain performance efficiency. An **Item** is represented as an array of values. **Items** are tied **Collections** and should be accessed and modified through the **Collection's** API.

# ItemCollection Usage

The **ItemCollection** is the base class for all other **Collections** and have a variety of useful methods to help analyze and process data.

- **get_item**: Takes an item name. Returns the item if it is stored in the collection.
- **get_item_names**: Returns a list of all item names stored in the collection.
- **add_attribute**: Takes an attribute and adds it to the set of all attributes that pertain to the current collection, updates the collection's items accordingly.
- **remove_attribute**: Takes an attribute name and removes it from the set of all attributes that pertains to the current collection. Removes attributes from all items pertaining to the collection as well.
- **contains**: Takes an item name. Returns True if that item is contained in the collection, false if not.
- **set_item_attribute**: Takes an item name, an attribute value, attribute name, and is descriptor which defaults to True. If the item already has an attribute by that name, overrides it, if not, then adds it to the item. Updates the entire collection to ensure each item has the same set of attributes.
- **get_item_attribute**: Takes an item name, and an attribute name. Returns the attribute if it exists in the given item name.
- **get_sorted**: Takes an attribute name, and a boolean value descending. Returns a list of tuples. The first item in the tuple will be the item name, the second item in the tuple will be the list of attributes pertaining to that item. If descending is False, returns in ascending order, else returns in descending order. Descending is set to False by default
- **merge_collections**: Takes a list of collections, and name. Merges this collection with the collections given and assigns the new merged collection to the name given. If collections share the same items, but the items have different attributes, then item attributes will be merged.
- **copy**: Returns a deep copy of the collection.
- **wipe**: Reset this collection.
- **strip**: Remove all attributes that have the same value for all items in the collection if the attribute is a descriptor. This can be useful for getting rid of noise.
- **from_csv**: Take a filename, an attribute start_row, an attribute start_column, a delimitter, an encoding, and a set of non descriptors. Imports the filename given to this collection, with attributes starting at the attribute start_row and attribute start_column given. If an attribute is imported that is also contained in the non descriptor set given, the attribute will be added as a non descriptor. Assumes that the start_column containing the item names is at start_column 0. Attribute start_row defaults to 0, attribute start_column defaults to 1, delimitter defaults to ',', non descriptos defaults to an empty set.
- **to_csv**: Takes a filename. Outputs the current collection to the given csv file.
- **random_forest_classification**:WIP
- **as_array**: Returns a pair. The first item will contain the array of the raw data for each item, while the second item will contain an array of item names that will correlate to the data array. The first array will contain lists of attributes that pertain to items. Only the attributes that are considered descriptors will be added. Useful for using this library in conjuction with others such as numpy, scipy, etc.
- **calc_rmse**: Takes a target score and an actual score. Both target score and actual score are attribute names. Returns the RMSE value of all items in the collection when comparing the value from their target score to their value in their actual score.
- **generate_error**: Takes a name, target score, and actual score. Both target score and actual score are attribute names. Takes the percent error of the value from the target score and actual score and generates a non descriptive attribute that will be stored at each item. The newly generated item's name will be the name passed.
- **calculate_similarity**: Take the name of two items, and returns their similarity score based on eculidean's algorithm.
- **calculate_all_similarities**: Takes an item name. Returns a list of tuples where the first value is the item the given item is being compared to, and the second value is the similarity score between to the two items. Will return similarity scores for all other items in the collection.
- **get_descriptive_attributes**: Return a list of all the descriptive attributes stored in this collection.
- **intersect**: Takes a collection. Returns a new collection that contains items located in both collections. Item attributes will be merged if the same item contains a set of different attributes.

# Cluster Usage

The **Cluster** is a class that stores items. It is utilized by the **ClusterCollection** and should rarely if ever be used in a raw fashion.

- **contains**: Take the name of an item and returns whether that item is stored in this cluster.
- **as_itemcollection**: Takes a boolean value copy. Returns an ItemCollection based on the cluster. Useful for if you want to export to a csv. If copy is set to True, will make a deep copy of the cluster. Copy is set to false by default.

# ClusterCollection Usage

The **ClusterCollection** is a child class of the **ItemCollection** class, and is utilized for clustering algorithms.

- **run_meanshift**: Run meanshift algorithm. Clusters will be generated for you.
- **run_kmean**: Run kmean algorithm. Will create as many clusters as ClusterCollection contains cluster_amount.
