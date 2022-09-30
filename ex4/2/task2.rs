fn main() {
    let test1 = String::from("foo <&> bar");
    let test2 = String::from("<<<<<<&&&&&>>>>>>>");
    let test3 = String::from("Cakes & cookies");
    let test4 = String::from("Rust > all other languages");
    
    println!("{}", replace(test1));
    println!("{}", replace(test2));
    println!("{}", replace(test3));
    println!("{}", replace(test4));
}

fn replace (str: String) -> String {
    let mut str_replacement = str.clone();
    str_replacement = str_replacement
        .replace("&", "&amp")
        .replace("<", "&lt")
        .replace(">", "&gt");
    
    return str_replacement;
}