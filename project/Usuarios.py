import psycopg2
from datetime import date, timedelta, datetime
import calendar

class User:

    def dbConnection(self):

        host = "172.17.0.2"
        dbname = "luisgym"
        user = "postgres"
        password = "mypassword"
        database_uri ="host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
        connection = psycopg2.connect(database_uri)

        return connection

    def obtenerUsuarios(self):
        query = "select id, trim(nombre), trim(apellidopat), trim(apellidomat), trim(telefono), estatus, trim(email), fechnat, fechregistro, fechavigencia, tipomembresia from usuarios;"

        response = {
            'registros': []
        }
        con = self.dbConnection()
        cursor = con.cursor()

        try:
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                obj = {
                    'id': i[0],
                    'nombre': i[1],
                    'apellidopat': i[2],
                    'apellidomat': i[3],
                    'telefono': i[4],
                    'estatus': i[5],
                    'email': i[6],
                    'fechnat': str(i[7]),
                    'fechregistro': str(i[8]),
                    'fechavigencia': str(i[9]),
                    'tipomembresia': i[10]

                }
                response['registros'].append(obj)
            
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            con.close()

        return response

    def selectActiveUsr(self):
        query = "select id, fechavigencia from usuarios where estatus = True;"

        response = {
            'registros': []
        }
        con = self.dbConnection()
        cursor = con.cursor()

        try:
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                obj = {
                    'id': i[0],
                    'fechavigencia': str(i[1])
                }
                response['registros'].append(obj)
            
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            con.close()

        return response

    def selectUsuario(self, id): 
        
        query = "select id, trim(nombre), trim(apellidopat), trim(apellidomat), trim(telefono), estatus, trim(email), fechnat, fechregistro, fechavigencia, tipomembresia from usuarios where id = %s;"

        response = {
            'registros': []
        }
        con = self.dbConnection()
        cursor = con.cursor()

        try:
            cursor.execute(query, (id,))

            res = cursor.fetchone()

            obj = {
                'id': res[0],
                'nombre': res[1],
                'apellidopat': res[2],
                'apellidomat': res[3],
                'telefono': res[4],
                'estatus': res[5],
                'email': res[6],
                'fechnat': str(res[7]),
                'fechregistro': str(res[8]),
                'fechavigencia': str(res[9]),
                'tipomembresia': res[10]

            }
            response['registros'].append(obj)
            
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            con.close()

        return response 

    def agregarUsuarios(self, usr):
        query = "INSERT INTO usuarios(nombre, apellidopat, apellidomat, telefono, email, fechnat, fechavigencia, tipomembresia) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;"
        
        response = {'id' : 0}
        print(usr)
        con = self.dbConnection()
        cursor = con.cursor()
        try:
            start_date = date.today()
            if int(usr['tipomembresia']) == 1:
                vigencia = start_date + timedelta(days=1)
            elif int(usr['tipomembresia']) == 2:
                vigencia = start_date + timedelta(days=7)
            elif int(usr['tipomembresia']) == 3:
                days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
                vigencia = start_date + timedelta(days=days_in_month)
            cursor.execute(query, (usr['nombre'], usr['apellidopat'], usr['apellidomat'], usr['telefono'], usr['email'], usr['fechnat'], vigencia, usr['tipomembresia']))
            id = cursor.fetchone()[0]
            response['id'] = int(id)
            con.commit()
            cursor.close()
            
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            con.close()
        return response

    def updateStatus(self, id, status):
        query = "UPDATE usuarios SET estatus = %s where id = %s;"

        con = self.dbConnection()
        cursor = con.cursor()
        try:
            cursor.execute(query, (status,id,))

            con.commit()
            
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            con.close()
        return True

    def updateUser(self, usr):
        query = """UPDATE usuarios SET name = %s, apellidopat = %s, apellidomat = %s, telefono = %s, 
                email = %s, fechnat = %s
                 where id = %s;"""

        con = self.dbConnection()
        cursor = con.cursor()
        try:
            cursor.execute(query, (usr['name'], usr['apellidopat'], usr['apellidomat'], usr['telefono'], usr['email'], usr['fechnat'],))

            con.commit()
            
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            con.close()
        return True

    def actualizarMembresia(self,usrid, tipo):

        start_date = date.today()
        end_date = start_date
        usr = self.selectUsuario(usrid)['registros'][0]
        vigencia = usr['fechavigencia']
        estatus = usr['estatus']
        vigencia = date(int(vigencia.split('-')[0]), int(vigencia.split('-')[1]), int(vigencia.split('-')[2]))

        if tipo == 1:
            if estatus:
                end_date = vigencia + timedelta(days=1)
            else:
                end_date = start_date + timedelta(days=1)
        elif tipo == 2:
            if estatus:
                end_date = vigencia + timedelta(days=7)
            else:
                end_date = start_date + timedelta(days=7)
        elif tipo == 3:
            days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
            if estatus:
                end_date = vigencia + timedelta(days=days_in_month)
            else:
                end_date = start_date + timedelta(days=days_in_month)

        query = "UPDATE usuarios SET fechavigencia = %s, estatus = %s where id = %s;"

        con = self.dbConnection()
        cursor = con.cursor()
        try:
            cursor.execute(query, (end_date, True, usrid,))

            con.commit()
            
        except Exception as ex:
            return {'error': str(ex)}
        finally:
            cursor.close()
            con.close()
            
        return { 'resp': True }
        
    def actualizaAllEstatus(self):

        try:
            usuarios = self.selectActiveUsr()['registros']
            curDate = date.today()
            
            for i in usuarios:
                vigencia = i['fechavigencia']
                vigencia = date(int(vigencia.split('-')[0]), int(vigencia.split('-')[1]), int(vigencia.split('-')[2]))
                if vigencia < curDate:
                    self.updateStatus(i['id'], False)

        except Exception as ex:
            return {'err': str(ex)}

        return { 'resp': True }

    def insertarMembresia(self, mem):
        query = "INSERT INTO tipomembresias(id, nombre, tipo, precio, duracion) VALUES(%s, %s, %s, %s, %s);"
        
        con = self.dbConnection()
        cursor = con.cursor()
        try:
            cursor.execute(query, (mem['id'], mem['nombre'], mem['tipo'], mem['precio'], mem['duracion']))

            con.commit()
            cursor.close()
            
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            con.close()
        return True
    # need to update the status afte the membership has expired
    def insertarAccion(self, obj):
        query = "INSERT INTO entradasysalidas(usuario, accion) VALUES(%s, %s);"

        con = self.dbConnection()
        cursor = con.cursor()
        try:
            cursor.execute(query, (obj['usuario'], obj['accion']))

            con.commit()
            cursor.close()
            
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            con.close()
        return { 'resp' : True }


u = User()
# if u.dbConnection():
#     print('cool!')
# print(u.obtenerUsuarios())
obj = {
    'nombre':'Jesus Uriel',
    'apellidopat': 'Sicairos',
    'apellidomat': 'Lopez',
    'telefono': '6672266013',
    'email': 'jesus.sicairos1@outlook.com',
    'fechnat': '1995-01-31',
    'fechavigencia': '2021-07-07',
    'tipomembresia': 3
}

memDia = {
    'id': 1,
    'nombre': 'Diario',
    'tipo': 'D',
    'precio': 30,
    'duracion': 1
}

memSem = {
    'id': 2,
    'nombre': 'Semanal',
    'tipo': 'S',
    'precio': 120,
    'duracion': 7
}

memMen = {
    'id': 3,
    'nombre': 'Mensual',
    'tipo': 'M',
    'precio': 300,
    'duracion': None
}

accEnt = {
    'usuario': 100001,
    'accion': 'E'
}
accSal = {
    'usuario': 100001,
    'accion': 'S'
}
# print(u.agregarUsuarios(obj))
# print(u.obtenerUsuarios())
# print(u.updateStatus(10000011, True))
# print(u.actualizarMembresia(10000011, 1))
# print(u.obtenerUsuarios())
# print(u.actualizaAllEstatus())
# print(u.insertarMembresia(memDia))
# print(u.insertarMembresia(memSem))
# print(u.insertarMembresia(memMen))
# print(u.insertarAccion(accSal))


