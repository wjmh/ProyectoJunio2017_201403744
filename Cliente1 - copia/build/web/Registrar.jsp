<%-- 
    Document   : Registrar
    Created on : 19/06/2017, 12:36:18 PM
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
       <h1>Registrar Usuario</h1>
        
        Registrar Usuario
        <form action="SRegistra" method="POST">
            <table border="0">
                <tbody>
                    <tr>
                        <td>Nickname</td>
                        <td><input type="text" name="txtnick" value="" /></td>
                    </tr>
                    <tr>
                        <td>Contraseña</td>
                        <td><input type="password" name="txtpass" value="" /></td>
                    </tr>
                    <tr>
                        <td>Correo</td>
                        <td><input type="text" name="txtcorreo" value="" /></td>
                    </tr>
                    <tr>
                        <td><input type="submit" value="Registrar" name="btnregistrar"  /></td>
                    </tr>
                    <tr>
                        
                        <td><input type="submit" value="Iniciar Sesion" name="btnsesion" /></td>
                    </tr>
                </tbody>
            </table>

            
        </form>
    </body>
</html>
