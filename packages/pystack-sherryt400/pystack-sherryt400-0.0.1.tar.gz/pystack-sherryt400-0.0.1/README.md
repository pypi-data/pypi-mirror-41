# pystack
Synchronized stack data structure for Python 3


**Usage**

```
from stack import Stack

stack = Stack()

# push item
stack.push('item')

# pop item
item = stack.pop()
```


**Define size**

```
stack = Stack(10)
```

**Producer Consumer example**

```
from stack import Stack

import random
from threading import Thread
from time import sleep

_stack = Stack(10)

item_number = 0


class Producer(Thread):
    __id = 1

    def __init__(self, stack: Stack):
        super().__init__(name='P-%d' % Producer.__id)
        self.__stack = stack
        Producer.__id = Producer.__id + 1
        pass

    def run(self):
        global item_number
        while (True):
            item = 'item_%d' % item_number
            self.__stack.push(item)
            print(self.name, ' produced ', item)
            item_number = item_number + 1
            sleep(random.randint(0, 1) * 0.3)


class Consumer(Thread):
    __id = 1

    def __init__(self, stack):
        super().__init__(name='C-%d' % Consumer.__id)
        self.__stack = stack
        Consumer.__id = Consumer.__id + 1
        pass

    def run(self):
        global item_number
        while (True):
            item = self.__stack.pop()
            print(self.name, ' consumed ', item)
            item_number = item_number - 1
            sleep(random.randint(0, 1) * 0.3)


p1 = Producer(_stack)
p2 = Producer(_stack)
p3 = Producer(_stack)
c1 = Consumer(_stack)
c2 = Consumer(_stack)
c3 = Consumer(_stack)

p1.start()
p2.start()
p3.start()
c1.start()
c2.start()
c3.start()
```

**LICENSE**

Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
