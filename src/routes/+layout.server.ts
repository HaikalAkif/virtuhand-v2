export async function load(props) {

    console.log(props.url)

    return {
        url: props.url.pathname
    }

}