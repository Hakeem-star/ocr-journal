<script lang="ts">
	import type { ChangeEventHandler, MouseEventHandler } from 'svelte/elements';

	let name = 'ocr test world';

	let uploadedImage: null | File = null;
	$: imageObjectURL = uploadedImage ? URL.createObjectURL(uploadedImage) : null;

	let ocrText = {
		aiResponse: '',
		rawResponse: ''
	};

	const handleChange: ChangeEventHandler<HTMLInputElement> = (e) => {
		console.log({ e }, 'change');
		const file = (e.target as HTMLInputElement)?.files?.[0];
		if (!file) return;
		uploadedImage = file;
		// uploadedImage = URL.createObjectURL(file);
		// # $ curl -F "image=@./assets/testocr.png" http://127.0.0.1:5000/generate-text

		const reader = new FileReader();
		reader.onload = (e) => {
			const img = new Image();
			img.src = e.target?.result as string;
			img.onload = () => {
				console.log(img.width, img.height);
			};
		};
		reader.readAsDataURL(file);
	};

	const handleSubmit: MouseEventHandler<HTMLButtonElement> = async (e) => {
		if (!uploadedImage) return;
		console.log('submit');
		const data = new FormData();
		data.append('file', uploadedImage, uploadedImage.name);

		const response = await fetch('http://localhost:5000/generate-text', {
			method: 'POST',
			body: data
			// headers: {
			// 	'Content-Type': 'multipart/form-data'
			// }
		});
		ocrText = await response.json();
	};
</script>

<div class="wrapper">
	<section>
		<h1>Welcome to {name}</h1>
		<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
		<div class="input_container">
			<input type="file" placeholder="Give me some of that OCR text" on:change={handleChange} />
		</div>

		<section class="ocr_image_section">
			<h2>OCR Image</h2>
			<p>Here is the uploaded image</p>

			{#if uploadedImage}
				<button type="submit" on:click={handleSubmit}>Convert to Text</button>
				<div class="img_wrapper">
					<img src={imageObjectURL} alt="uploaded" />
				</div>
			{/if}
		</section>
	</section>

	<section class="ocr_result_section">
		<h2>OCR Result Text</h2>
		<p>Here is the text that was extracted from the image</p>
		<p>{ocrText.aiResponse}</p>
		<p>{ocrText.rawResponse}</p>
	</section>
</div>

<style>
	.wrapper {
		display: flex;
	}

	section {
		width: 50%;
	}
	h1 {
		color: #ff3e00;
	}

	.input_container {
		width: fit-content;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		gap: 10px;
	}

	.ocr_image_section {
		/* padding-top: 15%; */
	}

	.img_wrapper {
		width: 100%;
		display: flex;
		justify-content: center;
		border: 2px solid black;
		aspect-ratio: 1;
	}

	.img_wrapper img {
		width: 100%;
		padding: 10px;
		object-fit: contain;
	}
</style>
