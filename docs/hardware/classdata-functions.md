# ClassData Functions

All plugin types that support media can use these callbacks to share information associated with their classID.

For example, these plugins can confirm their hardware is present and operational using the ClassData functions.

They all call `getClassData` during initialization. If `getClassData` returns 0, the module checks for and initialize the hardware.

It then calls setClassData to store information about the current context. Use handles, not pointers, for storing info.

```c++
typedef struct {
  SetClassDataFunc  setClassData;
  GetClassDataFunc  getClassData;
} ClassDataFuncs, *ClassDataFuncsPtr;
```

---

## Methods

### setClassData

`setClassData`

#### Description

Writes class data, destroys previous data.

Note that all plugins that share the data must use the same data structure.

```cpp
int setClassData (
    unsigned int  theClass,
    void          *info);
```

#### Parameters

| Parameter  |       Type        |                            Description                             |
| ---------- | ----------------- | ------------------------------------------------------------------ |
| `theClass` | Unsigned int      | The class being set. Use a unique 4-byte code.                    |
| `info`     | Pointer or handle | the class data to be set. It can be used as a pointer or a handle. |

---

### getClassData

`getClassData`

#### Description

Retrieves the class data for the given class.

```cpp
int getClassData (
    unsigned int  theClass);
```

#### Parameters

| Parameter  |       Type       |              Description              |
| ---------- | ---------------- | ------------------------------------- |
| `theClass` | Unsigned integer | The class for which to retrieve data. |
