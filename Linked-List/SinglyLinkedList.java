/**
 * Your implementation of a SinglyLinkedList
 *
 * @author John Blasco jblasco6
 * @version 1.0
 */
public class SinglyLinkedList<T extends Comparable<? super T>> implements
        LinkedListInterface<T> {
    // Do not add new instance variables.
    private SLLNode<T> head;
    private SLLNode<T> tail;
    private int size;

    @Override
    public void addToFront(T data) {
        if (data == null) {
            //Throw exception if data is null
            throw new java.lang.IllegalArgumentException("Input data is null.");
        }

        head = new SLLNode<T>(data, head);
        if (size == 0) {
            tail = head;
        }
        ++size;
    }

    @Override
    public void addAtIndex(T data, int index) {
        if (data == null) {
            throw new java.lang.IllegalArgumentException("Input data is null.");
        }
        if (index < 0 || index > size) {
            throw new java.lang.IndexOutOfBoundsException(
                    "Input index is out of bounds.");
        }

        if (index == 0) {
            addToFront(data);
        } else if (index == size) {
            addToBack(data);
        } else {
            SLLNode<T> current = head;
            for (int i = 0; i < index - 1; ++i) {
                current = current.getNext();
            }
            current.setNext(new SLLNode<T>(data, current.getNext()));
            ++size;
        }
    }

    @Override
    public void addToBack(T data) {
        if (data == null) {
            throw new java.lang.IllegalArgumentException("Input data is null.");
        }

        if (size == 0) {
            addToFront(data);
        } else {
            tail.setNext(new SLLNode<T>(data));
            tail = tail.getNext();
            ++size;
        }
    }

    @Override
    public T removeFromFront() {
        if (size == 0) {
            return null;
        } else {
            T temp = head.getData();
            head = head.getNext();
            if (size == 1) {
                tail = null;
            }
            --size;
            return temp;
        }
    }

    @Override
    public T removeAtIndex(int index) {
        if (index < 0 || index >= size) {
            throw new java.lang.IndexOutOfBoundsException(
                    "Input index is out of bounds.");
        }

        if (index == 0) {
            return removeFromFront();
        } else if (index == size - 1) {
            return removeFromBack();
        } else {
            SLLNode<T> current = head;
            T temp;

            for (int i = 0; i < index - 1; ++i) {
                current = current.getNext();
            }
            temp = current.getNext().getData();
            current.setNext(current.getNext().getNext());
            --size;
            return temp;
        }
        //return null;
    }

    @Override
    public T removeFromBack() {
        if (size == 0) {
            return null;
        } else if (size == 1) {
            return removeFromFront();
        } else {
            T temp = tail.getData();
            SLLNode<T> current = head;
            for (int i = 1; i < size - 1; ++i) {
                current = current.getNext();
            }
            current.setNext(null);
            tail = current;

            --size;
            return temp;
        }
    }

    @Override
    public T get(int index) {
        if (index < 0 || index >= size) {
            throw new java.lang.IndexOutOfBoundsException(
                    "Input index is out of bounds.");
        }

        if (index == 0) {
            return head.getData();
        } else if (index == size - 1) {
            return tail.getData();
        } else {
            SLLNode<T> current = head;
            for (int i = 0; i < index; ++i) {
                current = current.getNext();
            }

            return current.getData();
        }
    }

    @Override
    public T findLargestElement() {
        if (size == 0) {
            return null;
        }

        T temp = head.getData();
        SLLNode<T> current = head;

        while (current != null) {
            if (temp.compareTo(current.getData()) < 0) {
                temp = current.getData();
            }
            current = current.getNext();
        }

        return temp;
    }

    @Override
    public Object[] toArray() {
        Object[] arrayToReturn = new Object[size];
        SLLNode<T> current = head;

        for (int i = 0; i < size; ++i) {
            arrayToReturn[i] = current.getData();
            current = current.getNext();
        }
        return arrayToReturn;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public void clear() {
        head = null;
        tail = null;
        size = 0;
    }

    @Override
    public SLLNode<T> getHead() {
        // DO NOT MODIFY!
        return head;
    }

    @Override
    public SLLNode<T> getTail() {
        // DO NOT MODIFY!
        return tail;
    }
}
