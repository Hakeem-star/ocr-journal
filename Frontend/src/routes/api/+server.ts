export const actions = {
	default: async ({ cookies, request }) => {
		const data = await request.formData();

		const response = await fetch('http://localhost:5000/generate-text', {
			method: 'POST',
			body: data
		});
	}
};
