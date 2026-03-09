import java.io.*;
public class opcion1{
    public static void Productosmasvendidos(){
        BufferedReader brproductos=(new fileReader("productos.csv"));
        String linea brproductos.readLine();
        int MAX=100;
        int [] id=new int[MAX];
        String[] nombre=new int[MAX];
        String[] categoria=new int [MAX];
        Double[] precio=new Double[MAX];
        int[] vendedor_id=new int[MAX];

        int nProductos=0;
        while ((linea=brproductos.readLine()!=null)) {
            String[] datos=linea.split(",");
            id[nProductos]= Integer.Parseint(datos[0]);
            nombre[nProductos]=(datos[1]);
            categoria[nProductos]=(datos[2]);
            precio[nProductos]=Double.parseDouble(datos[3]);
            vendedor_id[nProductos]=Integer.parseInt(datos[4]);

            nProductos++;
        }
        brproductos.close();

        BufferedReader brpedidos=(new fileReader("pedidos.csv"));
        linea=brpedidos.readLine();
        while ((linea=brpedidos.readLine()!=null)) {
            String[] datos=linea.plit(",");
            int producto_id=Integer.parseInt(datos[3]);
            int cantidad=Integer.parseInt(datos[4]);

            for(int i=0,i< nProductos,i++){
                if(id==producto_id){
                    totalventas[i] += cantidad*precio[i];
                    break;
                }
            }
        }
        brpedidos.close();

        for(int i=0,i< nProductos-1,i++){
            for(int j=0,j< nProductos-1-i,j++){
                if(totalventas[j]<totalventas[j+1]){
                    totalventas temp=totalventas[j];
                    set(j,totalventas[j+1]);
                    set(j+1,temp);
                }
            }
        }
        System.out.println(producto_id,nombre,total);
        for(int i=0,i< nProductos, i++){
            if(totalventas[i]>0){
                System.out.println(id[i] + "," + nombre[i] + "," + totalventas[i]);
                System.out.println(id[i+1] + "," + nombre[i+1] + "," + totalventas[i+1]);
                System.out.println(id[i+2] + "," + nombre[i+2] + "," + totalventas[i+2]);
            }
        }




    }

}