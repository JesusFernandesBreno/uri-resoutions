package main

import "fmt" 

func main(){
	p1()
	p2()
	p3()
	p4()
	p5()
	p4()
	p3()
	p2()
	p1()
	
}

func p1(){
	fmt.Printf("       A\n")
}

func p2(){
	fmt.Printf("      B B\n")
}

func p3(){
	fmt.Printf("     C   C\n")
}

func p4(){
	fmt.Printf("    D     D\n")
}

func p5(){
	fmt.Printf("   E       E\n")
}