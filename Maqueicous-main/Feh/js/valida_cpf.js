var cpf = "169.169.000-75";
	cpf = "469.957.937-06";


	function isCPF(cpf = 0){
		console.log(cpf);
		cpf  = cpf.replace(/\.|-/g,"");
		console.log(cpf);
		if(!validaPrimeiroDigito(cpf))
		   return false;
		if(!validaSegundoDigito(cpf))
		   return false;

		return true;

	}
	var sum = 0;

	function validaPrimeiroDigito(cpf = null){
		let fDigit = (sumFristDigit(cpf) * 10) % 11;
		 	fDigit = (fDigit == 10 || fDigit == 11 ) ? 0 : fDigit; 
		if(fDigit != cpf[9])
			return false
    	return true;
	}
	function validaSegundoDigito(cpf = null){
		let sDigit = (sumSecondDigit(cpf) * 10) % 11;
	     	sDigit = (sDigit == 10 || sDigit == 11 ) ? 0 : sDigit;

		if(sDigit != cpf[10])
			return false
    	return true;
	}


	sumFristDigit = function(cpf, position=0, sum=0){
		if(position > 9)
			return 0;
		return sum + sumFristDigit(cpf,position+1,cpf[position] * ((cpf.length-1)-position));
	}


	sumSecondDigit = function(cpf, position=0, sum=0){
		if(position > 10)
			return 0;
		return sum + sumSecondDigit(cpf,position+1,cpf[position] * ((cpf.length)-position));
	}

console.log(isCPF(cpf));