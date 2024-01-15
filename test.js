const a = "test js file"

window.onload = () => {
  console.log('i am taking control');
};

function testInject() {
  console.log('I am injected js code');
}

testInject();
