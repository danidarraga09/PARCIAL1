import java.util.*;
    public class menu{
        public void Main (Strings[] args){

        try(Scanner sc= new Scanner(System.in)){
            int opcion=0;
        while(opcion!=5){
        System.out.println("----Sistema MarketHub----" );
        System.out.println("1.Mostrar los 3 productos más vendidos");
        System.out.println("2.Mostrar el vendedor con mayor facturación ");
        System.out.println("3.Mostrar las ventas totales por ciudad de clientes ");
        System.out.println("4.Buscar productos por categoría ordenados por precio ");
        System.out.println("5.Generar reporte de ventas por vendedor ");
        System.out.println("6.Salir");
        System.out.println("Digite una opcion");

        }
     

        opcion=sc.nextInt();
        switch (opcion) {
            case 1:
                
                break;
            case 2:
                break;
            
            case 3:
                break;
            
            case 4:
                break;

            case 5:
                break;

            case 6:
                System.out.println("Saliendo del Sistema");
            
            case 7:
            default:
                System.out.println("Opcion inválida");
            
        } 


       

    }  
}
    }