package main
import "fmt"
func main(){

	v := make([]rune, 3)
	for i := 0; i < 3; i++{
		fmt.Scanf("%s", &v[i])
	}

	for i := 0; i < 3; i++{
		fmt.Printf("->>> %s", string(v[i]))
	}
	
		
}