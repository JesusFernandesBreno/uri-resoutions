package main

import "fmt"

func main(){
	var qtdRunas, qtdDerrota int
	var runas = make(map[string]int)
	
	fmt.Scanf("%d %d", &qtdRunas, &qtdDerrota)

	var r string
	var v int
	for i := 0; i < qtdRunas; i++ {	
		fmt.Scanf("%s %d",&r, &v)
		runas[r] = v
	}

	var qtdInv int
	fmt.Scanf("%d", &qtdInv)

	runasInv := make([]string, qtdInv)
	
	for i := 0; i < qtdInv; i++ {
		fmt.Scanf("%s", &runasInv[i])
	}

	var tot int
	for _, key := range runasInv{
		tot += runas[key]
	}

	fmt.Printf("%d\n", tot)
	if tot >= qtdDerrota{
		fmt.Println("You shall pass!")
	}else{
		fmt.Println("My precioooous")
	}
	
}