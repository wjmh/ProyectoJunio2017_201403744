<%-- 
    Document   : index
    Created on : 18/06/2017, 09:05:00 PM
    Author     : william
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
       <h1 style="text-align: center">Login Usuario</h1>
        <form action="SValidar" method="POST">
            <table border="0" style="margin-left: 38%;">
                <tbody>
                    <tr>
                        <td>Usuario:</td>
                        <td><input type="text" name="txtnick" value="" /></td>
                    </tr>
                    <tr>
                        <td>Contraseña:</td>
                        <td><input type="password" name="txtpass" value="" /></td>
                    </tr>
                    <tr>
                        <td>Rol</td>
                        <td><select name="listarol">
                                <option value = "Jugador">Jugador</option>
                                <option value = "Administrador">Administrador</option>
                            </select></td>
                    </tr>
                    
                    <tr>
                        
                        <td><input type="submit" value="Iniciar Sesion" name="btnvalidar" /></td>
                        
                    </tr>
                   
                    <tr>         
                <td><input type="submit" value="Registrarse" name="btnregistrar" onclick="window.open('http://localhost:8080/Cliente1/Registrar.jsp')" /></td>
                        
                 </tr>   
                </tbody>
            </table>


            
        </form>
    </body>
</html>
