# ordered_set
 Ordered Set which is like a set, but retains the order of elements after logical operations.

## ordered_set.OrderedSet
Syntax:
```
OrderedSet(
    iterable: Iterable[Any]
)
```
Creates a set that retains the order of elements after logical operations.
For duplicated items, the order of the first element takes priority.

For example:
```
>>> set((1,2,3,4)) | set((1,2,9999999,16))
{1, 2, 3, 4, 16, 9999999}
```
The ordering of the elements were not preserved as this depends on their hash values.

```
>>> OrderedSet((1,2,3,4)) | OrderedSet((1,2,9999999,16))
OrderedSet((1, 2, 3, 4, 9999999, 16))
```
An OrderedSet preserves the order.

Supported operations: `&`, `|` and `^`.