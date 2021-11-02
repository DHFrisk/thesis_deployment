import decimal
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import Permission
import xlrd, xlsxwriter, io
from django.http import HttpResponse
import pandas as pd
from datetime import datetime

"""
FRONTEND VIEWS
"""
@login_required()
@require_http_methods(["GET"])
def view_add_equipo(request):
    if request.user.has_perm("equipo.add_equipo"):
        form = AddEquipoForm(initial={"user_creation":request.user.id})
        return render(request, "equipo/view_add_equipo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_equipo(request):
    if request.user.has_perm("equipo.view_equipo"):
        equipo= Equipo.objects.filter(is_active=True)
        return render(request, "equipo/view_view_equipo.html", {"equipo":equipo})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para ver equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_equipo(request):
    if request.user.has_perm("equipo.change_equipo"):
        equipo= Equipo.objects.filter(is_active=True)
        return render(request, "equipo/view_change_equipo.html", {"equipo":equipo})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_equipo(request, id):
    if request.user.has_perm("equipo.change_equipo"):
        equipo=Equipo.objects.get(id=id)
        form= ChangeEquipoForm(initial={"id":equipo.id, "code":equipo.code, "name":equipo.name, "user_edition":request.user.id, "accounting":equipo.accounting, "description":equipo.description, "brand":equipo.brand, "model":equipo.model, "unidad":equipo.fk_unidad, "assigned_user":equipo.fk_assigned_user, "header":equipo.header, "price":equipo.price, "asset_code":equipo.asset_code, "quantity":equipo.quantity})
        return render(request, "equipo/view_change_single_equipo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar equipo.", view="view_dashboard")



@login_required()
@require_http_methods(["GET"])
def view_delete_equipo(request):
    if request.user.has_perm("equipo.delete_equipo"):
        equipo=Equipo.objects.filter(is_active=True)
        return render(request, "equipo/view_delete_equipo.html", {"equipo":equipo})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_single_equipo(request, id):
    if request.user.has_perm("equipo.delete_equipo"):
        equipo=Equipo.objects.get(id=id)
        form= ChangeEquipoForm(initial={"id":equipo.id, "code":equipo.code, "name":equipo.name, "user_edition":request.user.id, "accounting":equipo.accounting, "description":equipo.description, "brand":equipo.brand, "model":equipo.model, "unidad":equipo.fk_unidad, "assigned_user":equipo.fk_assigned_user})
        return render(request, "equipo/view_delete_single_equipo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_deactivate_single_equipo(request, id):
    if request.user.has_perm("equipo.delete_equipo"):
        equipo=Equipo.objects.get(id=id)
        form= DeactivateEquipoForm(initial={"id":equipo.id, "code":equipo.code, "name":equipo.name, "user_edition":request.user.id, "accounting":equipo.accounting, "description":equipo.description, "brand":equipo.brand, "model":equipo.model, "unidad":equipo.fk_unidad, "assigned_user":equipo.fk_assigned_user})
        return render(request, "equipo/view_delete_single_equipo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_add_incomes_header(request):
    if request.user.has_perm("equipo.add_equipo"):
        form=AddHeaderForm()
        return render(request, "equipo/view_add_incomes_header.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para registrar entradas.", view="view_dashboard")



############################################################################

@login_required()
@require_http_methods(["GET"])
def view_add_accounting(request):
    if request.user.has_perm("equipo.add_accounting"):
        form = AddAccountingForm(initial={"user_creation":request.user.id})
        return render(request, "equipo/view_add_accounting.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_accounting(request):
    if request.user.has_perm("equipo.view_accounting"):
        accounting= Accounting.objects.filter(is_active=True)
        return render(request, "equipo/view_view_accounting.html", {"accounting":accounting})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para ver equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_accounting(request):
    if request.user.has_perm("equipo.change_accounting"):
        accounting= Accounting.objects.filter(is_active=True)
        return render(request, "equipo/view_change_accounting.html", {"accounting":accounting})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_accounting(request, id):
    if request.user.has_perm("equipo.change_accounting"):
        accounting = Accounting.objects.get(id=id)
        form= ChangeAccountingForm(initial={"id":accounting.id, "name":accounting.name, "user_edition":request.user.id})
        return render(request, "equipo/view_change_single_accounting.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar equipo.", view="view_dashboard")



@login_required()
@require_http_methods(["GET"])
def view_delete_accounting(request):
    if request.user.has_perm("equipo.delete_accounting"):
        accounting= Accounting.objects.filter(is_active=True)
        return render(request, "equipo/view_delete_accounting.html", {"accounting":accounting})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar equipo.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_deactivate_single_accounting(request, id):
    if request.user.has_perm("equipo.delete_accounting"):
        accounting = Accounting.objects.get(id=id)
        form = DeactivateAccountingForm(initial={"id": accounting.id, "name": accounting.name, "user_edition": request.user.id})
        return render(request, "equipo/view_delete_single_accounting.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar equipo.", view="view_dashboard")




"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_add_equipo(request):
    if request.user.has_perm("equipo.add_equipo"):
        try:
            form= AddEquipoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Equipo registrado exitosamente.", view="view_add_equipo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_add_equipo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar equipo.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_change_single_equipo(request):
    if request.user.has_perm("equipo.change_equipo"):
        try:
            form= ChangeEquipoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Equipo modificado exitosamente.", view="view_change_equipo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_change_equipo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar equipo.", view="view_dashboard")



@require_http_methods(["POST"])
def backend_deactivate_single_equipo(request):
    if request.user.has_perm("equipo.delete_equipo"):
        try:
            form= DeactivateEquipoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Equipo anulado exitosamente.", view="view_delete_equipo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al anular de datos, intente de nuevo", view="view_delete_equipo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para anular equipo.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_delete_single_equipo(request):
    if request.user.has_perm("equipo.delete_equipo"):
        try:
            form= DeleteEquipoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Equipo eliminado exitosamente.", view="view_delete_equipo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al eliminar de datos, intente de nuevo", view="view_delete_equipo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar equipo.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_add_incomes_header(request):
    if request.user.has_perm("equipo.add_equipo"):
        # u= User.objects.get(id=reques)
        try:
            form= AddHeaderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Equipo eliminado exitosamente.", view="view_dashboard")
                # return redirect("alert", message_type="success", message= "Equipo eliminado exitosamente.", view="view_incomes_headers")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar entradas.", view="view_dashboard")

################################################################################################################

@require_http_methods(["POST"])
def backend_add_accounting(request):
    if request.user.has_perm("equipo.add_accounting"):
        try:
            form = AddAccountingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message="Cuenta registrada exitosamente.",
                                view="view_add_accounting")
            else:
                return redirect("alert", message_type="warning",
                                message="Ha ocurrido un error en el ingreso de datos, intente de nuevo",
                                view="view_add_accounting")
        except Exception as e:
            return redirect("alert", message_type="error", message=f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message="No tiene los permisos necesarios para agregar cuentas.",
                        view="view_dashboard")


@require_http_methods(["POST"])
def backend_change_single_accounting(request):
    if request.user.has_perm("equipo.change_accounting"):
        try:
            form = ChangeAccountingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message="Cuenta modificada exitosamente.",
                                view="view_change_accounting")
            else:
                return redirect("alert", message_type="warning",
                                message="Ha ocurrido un error en el ingreso de datos, intente de nuevo",
                                view="view_change_accounting")
        except Exception as e:
            return redirect("alert", message_type="error", message=f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error",
                        message="No tiene los permisos necesarios para modificar cuentas.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_deactivate_single_accounting(request):
    if request.user.has_perm("equipo.delete_accounting"):
        try:
            form = DeactivateAccountingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message="Cuenta anulada exitosamente.",
                                view="view_delete_accounting")
            else:
                return redirect("alert", message_type="warning",
                                message="Ha ocurrido un error al anular de datos, intente de nuevo",
                                view="view_delete_accounting")
        except Exception as e:
            return redirect("alert", message_type="error", message=f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message="No tiene los permisos necesarios para anular cuentas.",
                        view="view_dashboard")

#####################################################################################################
@login_required()
@require_http_methods(["POST"])
def write_responsibility_sheet(request, equipment_id):
    '''
    generate a responsiblity little report that shows the current values assigned or related to a specific asset (equipo)
    '''
    equipment= Equipo.objects.get(id=equipment_id)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    sheet = workbook.add_worksheet()
    sheet.set_column(1, 3, 40)
    # sheet.set_column("C",30)
    # sheet.set_row(3, 30)
    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'yellow'})
    sheet.merge_range("A1:A3", "Logo", merge_format)
    sheet.merge_range("B1:D2", "CONTROL DE DESCARGO Y CARGO DEL REGUARDO DE BIENES", merge_format)
    sheet.merge_range("B3:D3", "Del proceso: Inventarios     Código: INV-FOR-043     Versión: 1     Página 1 de 1", merge_format)
    sheet.merge_range("B5:D5", "Datos tabla 1", merge_format)
    sheet.merge_range("B10:D10", "Datos tabla 2", merge_format)

    sheet.merge_range("B6:D6",
                      "El (los) artículo (s) que en este formulario aparece (n), se descargarán del  resguardo de bienes a cargo de:",
                      merge_format)
    sheet.merge_range("B11:D11", "Y serán cargados en el resguardo de responsabilidad a cargo de: ", merge_format)

    # sheet.write(5,2,"El (los) artículo (s) que en este formulario aparece (n), se descargarán del  resguardo de bienes a cargo de:")
    sheet.write(6, 1, "Nombre completo")
    if equipment.fk_last_assigned_user != None and equipment.fk_last_unidad != None:
        sheet.write(6, 2, equipment.fk_last_assigned_user.first_name+" "+equipment.fk_assigned_user.last_name)
        sheet.write(7, 2, equipment.fk_last_unidad.name)
    else:
        sheet.write(6, 2, "No existe un usuario asignado anteriormente")
        sheet.write(7, 2, "No existe una unidad asignada con anterioridad")
    sheet.write(7, 1, "Unidad ejecutora")
    sheet.write(8, 1, "Numero de resguardo")

    # sheet.write(10,2,"Y serán cargados en el resguardo de responsabilidad a cargo de: ")
    sheet.write(11, 1, "Nombre completo")
    sheet.write(11, 2, equipment.fk_assigned_user.first_name+" "+equipment.fk_assigned_user.last_name)
    sheet.write(12, 1, "Unidad ejecutora")
    sheet.write(12, 2, equipment.fk_unidad.name)
    sheet.write(13, 1, "Numero de resguardo")

    # sheet.write()
    # sheet.write("")

    workbook.close()
    output.seek(0)
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'ficha_responsabilidad.xlsx'
    return response


def write_general_report(request):
    '''
    generate a big accounting report based on the intitution assets (and as usual related or assigned information to every asset listed) filtered, organized and grouped by the accounting type/name
    '''
    #getting essential info/registers/data
    df_list = Equipo.objects.all().values_list("date_creation",
                                               "id",
                                               "code",
                                               "name",
                                               "accounting__name",
                                               "description",
                                               "brand",
                                               "model",
                                               "price",
                                               "reference",
                                               "is_active",
                                               "is_in_storage").order_by("accounting__name")

    #creating the data frame and filling it with the data
    df = pd.DataFrame(df_list,
                      columns=["Fecha",
                               "id",
                               "Codigo",
                               "Nombre",
                               "Cuenta",
                               "Descripcion",
                               "Marca",
                               "Modelo",
                               "Precio",
                               "Referencia",
                               "Activo",
                               "En bodega"])
    df["Fecha"]=pd.to_datetime(df["Fecha"])
    df["Fecha"]=df["Fecha"].dt.strftime("%d/%M/%Y")
    df.set_index("id")
    alzas_column=[]
    bajas_column=[]

    #start grouping equipment based if it is 'Active' or not (basically if is active is an addition of money and if not is a substraction of money)
    for index, row in df.iterrows():
        if row["Activo"] == True:
            alzas_column.append({"id":row["id"], "value":row["Precio"]})
        else:
            bajas_column.append({"id":row["id"], "value":row["Precio"]})

    #adding 2 columns to the dataset (additions and substractions) which are null at their craetion
    df["Alzas"]=None
    df["Bajas"]=None

    #filling newly created columns based on current state of equipment
    for i in alzas_column:
        index = df.index[df["id"] == i["id"]]
        index=index.item()
        df.loc[index, "Alzas"] = i["value"]
    for i in bajas_column:
        index = df.index[df["id"] == i["id"]]
        index=index.item()
        df.loc[index, "Bajas"] = i["value"]

    #create new column, result of additions and substractions of money based in equipment
    df["Total"]=decimal.Decimal(0)

    #filling the results column of money
    for index, row in df.iterrows():
        if index > 0:
            last_value= df.loc[index-1, "Total"]
            current_value= {"is_positive":True, "value":row["Alzas"]} if row["Alzas"] != None else {"is_positive":False, "value":row["Bajas"]}
            df.loc[index, "Total"]= current_value["value"]+last_value if current_value["is_positive"] else -current_value["value"]+last_value
        else:
            current_value = {"is_positive": True, "value": row["Alzas"]} if row["Alzas"] != None else {"is_positive": False, "value": row["Bajas"]}
            df.loc[index, "Total"] = current_value["value"] if current_value["is_positive"] else -current_value["value"]

    #get the accounting registers ordered by name
    accounts=Accounting.objects.all().values_list("name").order_by("name")

    #creating another dataframe with the finally output data
    acc_df=pd.DataFrame(columns=["Fecha","id","Codigo","Nombre","Cuenta","Descripcion","Marca","Modelo","Precio","Referencia","Activo","En bodega","Alzas","Bajas","Total"])

    #filling the new dataframe with the final values
    for acc in accounts:
        acc_row= {"Fecha":"--------",
                  "id":000000000000,
                  "Codigo":"--------",
                  "Nombre":"--------",
                  "Cuenta":acc[0],
                  "Descripcion":acc[0],
                  "Marca":"--------",
                  "Modelo":"--------",
                  "Precio":decimal.Decimal(0),
                  "Referencia":"--------",
                  "Activo":"--------",
                  "En bodega":"--------",
                  "Alzas":decimal.Decimal(0),
                  "Bajas":decimal.Decimal(0),
                  "Total":decimal.Decimal(0)}
        #append the accounting 'title'/name
        acc_df=acc_df.append(acc_row, ignore_index=True)
        #append all rows that match with the current accounting name
        acc_df=acc_df.append(df[df["Cuenta"]==acc[0]], ignore_index=True)

    for index, row in acc_df.iterrows():
        if row["Codigo"]=="--------" and row["Nombre"]=="--------":
            acc_df.loc[index, "Descripcion"]=row["Cuenta"]
        else:
            acc_df.loc[index, "Descripcion"]="Codigo: "+str(row["Codigo"])+\
                                              ", Nombre: "+row["Nombre"]+\
                                              ", Descripcion: "+row["Descripcion"]+\
                                              ", Marca: "+row["Marca"]+\
                                              ", Modelo: "+row["Modelo"]+\
                                              ", Precio: "+str(row["Precio"])+\
                                              ", Referencia: "+row["Referencia"]

    #remove crap columns
    acc_df=acc_df.drop(["Codigo", "Nombre", "Cuenta", "Marca", "Modelo", "Precio", "Referencia", "En bodega", "id", "Activo"], axis=1)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=reporte_general.csv'
    acc_df.to_csv(path_or_buf=response, index=False)
    return response
