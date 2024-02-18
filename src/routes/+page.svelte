<script lang="ts">
	import { enhance } from '$app/forms';
	import '$lib/style.css';

	const { form } = $props();
</script>

<div class="wrapper">
	<h1 class="main">DARETRUTH</h1>

	<form
		action="/"
		method="POST"
		use:enhance={() => {
			return async ({ update }) => {
				update({ reset: false });
			};
		}}
	>
		<div class="level">
			{#each [1, 2, 3, 4, 5] as index}
				<input
					type="radio"
					name="level"
					id={`l${index}`}
					value={index}
					checked={(form?.level ?? 1) === index}
				/>
				<label for={`l${index}`} class="level__label">{index}</label>
			{/each}
			<div class="level__indicator"></div>
		</div>

		<br />

		<div class="submitwrapper">
			<input type="submit" name="tod" value="truths" class="pure-button fuller-button blue" />
			<p class="fuller-button">OR</p>
			<input type="submit" name="tod" value="dares" class="pure-button fuller-button red" />
		</div>
	</form>

	<h1>{form?.newDare}</h1>
</div>
