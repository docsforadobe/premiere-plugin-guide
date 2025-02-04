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

|    Function    |                                                                                                                                                                                          Description                                                                                                                                                                                          |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `setClassData` | Writes class data, destroys previous data.<br /><pre>int setClassData (<br/>  unsigned int  theClass,<br/>  void          *info);<br/></pre><ul><li>`theClass` - the class being set. Use a unique 4-byte code.</li><li>`info` - the class data to be set. It can be used as a pointer or a handle.</li></ul><br/>Note that all plugins that share the data must use the same data structure. |
| `getClassData` | Retrieves the class data for the given class.<br /><pre>int getClassData (<br/>  unsigned int  theClass);<br/></pre><ul><li>`theClass` - the class for which to retrieve data.</li></ul>                                                                                                                                                                                                      |
