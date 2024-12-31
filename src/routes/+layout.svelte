<script lang="ts">
	import '../app.css';
	let {data, children} = $props();

	console.log(data)

</script>

<!-- {#key data.url}
<div
	class="h-full w-full"
	in:fly={{ x: -200, duration: 300, delay: 200 }}
	out:fly={{ x: 200, duration: 300 }}
> -->
{@render children()}
<!-- </div>
{/key} -->
