function errorAlert(error){
	Swal.fire({
	  title: '¡Error!',
	  text: 'Ha ocurrido un error: '+ error,
	  icon: 'error',
	  confirmButtonText: 'Cool'
	});
}

function successAlert(text){
	Swal.fire({
	  title: '¡Éxito!',
	  text: 'Se ha realizado exitosamente la acción: '+text,
	  icon: 'success',
	  confirmButtonText: 'Cool'
	});
}

function questionAlert(text){
	Swal.fire({
	  title: '¿Está seguro?',
	  text: 'Desea realizar la acción: '+text,
	  icon: 'question',
	  confirmButtonText: 'Cool'
	});
}