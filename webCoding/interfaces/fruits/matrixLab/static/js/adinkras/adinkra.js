

function AdinkraA() {
  return <div>
      <h2>adinkra</h2>
      <div className={"container4"}>
          <div className={"vertices"}>
          </div>

      </div>
  </div>
}

function AdinkraB() {

  return <div>
      <h2>adinkra</h2>
      <div className={"container4"}>
      <div className={"animation-target"}>
</div>

      </div>
  </div>
}

function Select(props) {
  const select = props.select;
  if (select) {
    return <AdinkraA />;
  }
  return <AdinkraB />;
}

ReactDOM.render(
  <Select select={false} />,
  document.getElementById('root')
);
