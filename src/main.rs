fn main() {
    let hw = "Hello World!";
    for _ in hw.replace(" ", "").strip_suffix("!").unwrap().chars() {
        println!("{hw}");
    }
}
