/**
 * @name py34_cwe_079
 * @description py3_cwe_079
 * @kind problem
 * @problem.severity error
 * @security-severity 6.1
 * @precision medium
 * @id py_1
 * @tags security
 *       
 */
import python
predicate isVulnerableName(Name  name) {
    // (
        name.getId()="path"
        and
        name.getParentNode() instanceof Call
        and
      (
        name.getParentNode().(Call).getAnArg().(BinaryExpr).getAChildNode().(Str).getText().toString().regexpMatch(".*<a href=.*")
        or
        name.getParentNode().(Call).getAnArg().(Call).getAChildNode().(Attribute).getAChildNode().(Str).getText().toString().regexpMatch(".*<span class.*")
      )  
        
    // )
    

  }

predicate  isSafeName( Name name) {
    name.getId()="format_html"
    and
    name.getParentNode() instanceof Call

}


 Stmt isSafeStmt(Stmt s_safe,Name name_vul,Name name_safe) {

    s_safe=name_safe.getScope().getBody().getAnItem()
    and
    s_safe.contains(name_safe)
    and
    s_safe!=name_vul.getScope().getBody().getAnItem()
    and
    result=s_safe
  }


  Stmt isVulStmt(Stmt s_vul,Name name_vul,Name name_safe) {

    s_vul=name_vul.getScope().getBody().getAnItem()
    and
    s_vul.contains(name_vul)
    and
    s_vul!=name_vul.getScope().getBody().getAnItem()
    and
    result=s_vul
  }

predicate s_vul_types(Stmt s_vul) {
     s_vul instanceof AssignStmt
     or
     s_vul instanceof Return
    //  or
    //  s_vul instanceof For
}

from Name name_vul,Name name_safe,Stmt s_vul,Stmt s_safe
where

isVulnerableName(name_vul)
and
isSafeName(name_safe)
and
s_vul=name_vul.getScope().getBody().getAnItem()
and
s_vul.contains(name_vul)
and
s_vul!=isSafeStmt(s_safe, name_vul, name_safe)
// and
// s_vul_types(s_vul)

select s_vul, "",s_vul.getLocation()
// ,


// from ExprStmt exstmt
// where

// exstmt.getValue().(Call).getAChildNode().(Attribute).getName().toString().regexpMatch(".*write.*")  
// and
// exstmt.getValue().(Call).getAChildNode().(Attribute).getObject().toString().regexpMatch(".*self.*")
// and
// exstmt.getValue().(Call).getAnArg().(Fstring).getAChildNode().(Name).getId().regexpMatch(".*path.*")

// select exstmt, "Found call to self.write with specific error message pattern."

// // exstmt.getValue().(Call).getAChildNode().(Attribute).getObject().(Name).getId().regexpMatch(".*self.*")