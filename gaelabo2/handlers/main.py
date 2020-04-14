#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from datetime import datetime


class MainHandler(webapp2.RequestHandler):
    def post(self):
        nombre = self.request.get("edNombre")
        cif = self.request.get("edCIF")
        direccion = self.request.get("edDireccion")
        poblacion = self.request.get("edPoblacion")
        provincia = self.request.get("edProvincia")
        cp = self.request.get("edCP")
        pais = self.request.get("edPais")
        contacto = self.request.get("edContacto")
        email = self.request.get("edEmail")
        telefono = self.request.get("edTelefono")
        nombreCliente = self.request.get("edNombreCliente")
        cifCliente = self.request.get("edCIFCliente")
        direccionCliente = self.request.get("edDireccionCliente")
        poblacionCliente = self.request.get("edPoblacionCliente")
        provinciaCliente = self.request.get("edProvinciaCliente")
        cpCliente = self.request.get("edCPCliente")
        paisCliente = self.request.get("edPaisCliente")
        contactoCliente = self.request.get("edContactoCliente")
        emailCliente = self.request.get("edEmailCliente")
        telefonoCliente = self.request.get("edTelefonoCliente")
        concepto = self.request.get("edConcepto")
        precio = self.request.get("edPrecio")
        unidades = self.request.get("edUnidad")
        importeBruto = self.request.get("edImporteBruto")
        porcentaje = self.request.get("edPorcentaje")
        importeTotal = self.request.get("edImporteTotal")
        fechaActual = datetime.now().date()

        if len(nombre.strip()) == 0:
            nombre = "Desconocido"
        if len(cif.strip()) == 0:
            cif = "Desconocido"
        if len(direccion.strip()) == 0:
            direccion = "Desconocido"
        if len(poblacion.strip()) == 0:
            poblacion = "Desconocido"
        if len(provincia.strip()) == 0:
            provincia = "Desconocido"
        if len(cp.strip()) == 0:
            cp = "Desconocido"
        if len(pais.strip()) == 0:
            pais = "Desconocido"
        if len(contacto.strip()) == 0:
            contacto = "Desconocido"
        if len(email.strip()) == 0:
            email = "Desconocido"
        if len(telefono.strip()) == 0:
            telefono = "Desconocido"
        if len(nombreCliente.strip()) == 0:
            nombreCliente = "Desconocido"
        if len(cifCliente.strip()) == 0:
            cifCliente = "Desconocido"
        if len(direccionCliente.strip()) == 0:
            direccionCliente = "Desconocido"
        if len(poblacionCliente.strip()) == 0:
            poblacionCliente = "Desconocido"
        if len(provinciaCliente.strip()) == 0:
            provinciaCliente = "Desconocido"
        if len(cpCliente.strip()) == 0:
            cpCliente = "Desconocido"
        if len(paisCliente.strip()) == 0:
            paisCliente = "Desconocido"
        if len(contactoCliente.strip()) == 0:
            contactoCliente = "Desconocido"
        if len(emailCliente.strip()) == 0:
            emailCliente = "Desconocido"
        if len(telefonoCliente.strip()) == 0:
            telefonoCliente = "Desconocido"
        if len(concepto.strip()) == 0:
            concepto = "Desconocido"
        if len(precio.strip()) == 0:
            precio = "Desconocido"
        if len(unidades.strip()) == 0:
            unidades = "Desconocido"
        if len(importeBruto.strip()) == 0:
            importeBruto = "Desconocido"
        if len(porcentaje.strip()) == 0:
            porcentaje = "Desconocido"
        if len(importeTotal.strip()) == 0:
            importeTotal = "Desconocido"

        factura_values = {
            'fechaActual': fechaActual,
            'nombre': nombre,
            'cif': cif,
            'direccion': direccion,
            'poblacion': poblacion,
            'provincia': provincia,
            'cp': cp,
            'pais': pais,
            'contacto': contacto,
            'email': email,
            'telefono': telefono,
            'nombreCliente': nombreCliente,
            'cifCliente': cifCliente,
            'direccionCliente': direccionCliente,
            'poblacionCliente': poblacionCliente,
            'provinciaCliente': provinciaCliente,
            'cpCliente': cpCliente,
            'paisCliente': paisCliente,
            'contactoCliente': contactoCliente,
            'emailCliente': emailCliente,
            'telefonoCliente': telefonoCliente,
            'concepto': concepto,
            'precio': precio,
            'unidades': unidades,
            'importeBruto': importeBruto,
            'porcentaje': porcentaje,
            'importeTotal': importeTotal
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("factura.html", **factura_values))


app = webapp2.WSGIApplication([
    ('/factura', MainHandler)
], debug=True)
