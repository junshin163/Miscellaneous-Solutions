public class TwoStackQueue<T> {
	
	private MyStack<T> s1;
	private MyStack<T> s2;
	
	public TwoStackQueue(){
		s1 = new MyStack<>();
		s2 = new MyStack<>();
	}
	
	public void enqueue(T x){
		s1.push(x);
	}
	
	public T dequeue(){
		if(s1.size() == 0 && s2.size() == 0){
			System.out.println("Cannot dequeue empty queue");
		}
		if(s2.size() != 0){
			return s2.pop();
		}
		else{
			for(int i = 0; i < s1.size() + s2.size(); i++){
				s2.push(s1.pop());
			}
			return s2.pop();
		}
	}
	
	public int size(){
		return (s1.size() + s2.size());
	}
	
	public boolean isEmpty(){
		return (s1.size() == 0 && s2.size() == 0);
	}
	
	public String toString(){
		return "Stack 1: " + s1 + "\n" + "Stack 2: " + s2;
	}
}
