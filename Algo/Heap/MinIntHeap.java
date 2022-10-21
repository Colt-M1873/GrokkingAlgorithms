/** from https://www.youtube.com/watch?v=t0Cq6tVNRBA&list=PLyN7oxIwNU8H2DuUHcf86zDc0k2SajSon&ab_channel=HackerRank */

import java.awt.*;
import java.util.Arrays;

public class MinIntHeap {// with limited, constant capacity
    private int capacity=10;
    private int size=0;
    int[] items=new int[capacity];

    /**Helper Methods*/
    private int getLeftChildIndex(int parentIdx){return 2*parentIdx+1;}
    private int getRightChildIndex(int parentIdx){return 2*parentIdx+2;}
    private int getParentIndex(int childIdx){return (childIdx-1)/2;}

    private boolean hasLeftChild(int idx){return getLeftChildIndex(idx)<size;}
    private boolean hasRightChild(int idx){return getRightChildIndex(idx)<size;}
    private boolean hasParent(int idx){return getParentIndex(idx)>=0;}

    private int leftChild(int idx){return items[getLeftChildIndex(idx)];}
    private int rightChild(int idx){return items[getRightChildIndex(idx)];}
    private int parent(int idx){return items[getParentIndex(idx)];}

    private void swap(int indexOne,int indexTwo){
        int tmp=items[indexOne];
        items[indexOne]=items[indexTwo];
        items[indexTwo]=tmp;
    }

    private void ensureExtraCapacity(){
        if (size==capacity){
            items= Arrays.copyOf(items,capacity*2);
            capacity*=2;
        }
    }

    public int peek(){
        if (size==0) throw new IllegalStateException();
        return items[0];
    }

    /** Delete the root(first) item */
    public int poll(){
        if (size==0) throw new IllegalStateException();
        int item=items[0];
        items[0]=items[size-1];
        size--;
        heapifyDown();
        return item;
    }

    public void add(int item){
        ensureExtraCapacity();
        items[size]=item;
        size++;
        heapifyUp();
    }

    public void heapifyDown(){
        int index=0;
        while (hasLeftChild(index)) {
            int smallerChildIdx=getLeftChildIndex(index);
            if (hasRightChild(index) && rightChild(index)<leftChild(index)) {
                smallerChildIdx=getRightChildIndex(index);
            }
            if (items[index]>items[smallerChildIdx]){
                swap(smallerChildIdx,index);
                index=smallerChildIdx;
            }
        }
}


    public void heapifyUp(){
        int index = size-1;
        while (hasParent(index) && parent(index)>items[index]){
            swap(getParentIndex(index),index);
            index=getParentIndex(index);
        }
    }

    public void printHeap(){
        for (int i=0;i<size;i++){
            System.out.print(items[i]);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        MinIntHeap h=new MinIntHeap();
        h.add(1);
        h.add(2);
        h.add(3);
        h.printHeap();
        h.add(5);
        h.add(0);
        h.printHeap();
    }
}