public class MyStack<T> implements MyStackInterface<T> {
	private T[] stackArray;
	private int size;
	private int capacity;
	
	public MyStack(){
		capacity = 10;
		stackArray = (T []) new Object[capacity];
		size = 0;
	}
	
	public void push(T x){
		if(size == capacity){
			expand();
		}
		stackArray[size] = x;
		size++;
	}
	
	public T pop(){
		if(size == 0){
			System.out.println("Stack Underflow");
			return null;
		}
		size--;
		return stackArray[size];
	}
	
	public T peek(){
		return stackArray[size - 1];
	}
	
	public boolean isEmpty(){
		return (size == 0);
	}
	
	public int size(){
		return size;
	}
	
	public void expand(){
		capacity *= 2;
		T[] temp = (T []) new Object[capacity];
		for(int i = 0; i < size; i++){
			temp[i] = stackArray[i];
		}
		stackArray = temp;
	}
	
	public String toString(){
		String returnedString = "";
		for(int i = 0; i<size; i++){
			returnedString = returnedString + stackArray[i] + " ";
		}
		return returnedString;
	}
}
