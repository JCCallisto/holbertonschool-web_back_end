export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      // When promise resolves successfully
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success'
      };
    })
    .catch(() => {
      // When promise rejects
      console.log('Got a response from the API');
      return new Error();
    })
    .finally(() => {
      // This runs regardless of resolve/reject
      console.log('Got a response from the API');
    });
}
