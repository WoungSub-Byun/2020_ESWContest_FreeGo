import React from 'react';

function MainContainer() {

	const LoadData = (kind) => {

		if (kind === "search"){

		} else {

		}
		
		//axios를 사용하여 서버에서 조회한 값
		const result = {
			"code": 200,
			"data": [
				{
					"id": "내 냉장고1",
					"p_ex_date": "Mon, 31 Aug 2020 00:00:00 GMT",
					"p_name": "가지",
					"p_number": 4
				}
			],
			"message": "select success"
		};

		if (result.code === 200){
			return result.data
		}

	}

	const LoadComponent = () => {

	}

	const

	return (
		<div>
			<SearchBar value={} />
			{LoadComponent}
		</div>
	);
}
export default MainContainer;
