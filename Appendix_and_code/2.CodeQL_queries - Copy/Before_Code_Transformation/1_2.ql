/**
 * @name py_67_80__cwe_079
 * @description py_cwe_079
 * @kind problem
 * @problem.severity error
 * @security-severity 6.1
 * @precision medium
 * @id py_1
 * @tags security
 *       
 */
import python

predicate isFixed(Name name_fixed) {
  // (
  //   // py_1
  //   name_fixed.getId()="document"
  //   and
  //   name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(0).(Str).getText() ="<a href=\"{}\">{} <span class=\"meta\">({}, {})</span></a>"
  //   and
  //   name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(1).(Attribute).getAChildNode().(Name).getId()="document"
  //   and
  //   name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(2).(Attribute).getAChildNode().(Name).getId()="document"
  //   and
  //   name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(3).(Call).getAChildNode().(Attribute).getAttr()="upper"
  // )
  // or
  // // py_2
  // (
  //   name_fixed.getId()="bits"
  //   and
  //   name_fixed.getParentNode().(Call).getAChildNode().(Attribute).getAttr()="join"
  //   and
  //   name_fixed.getParentNode().(Call).getAChildNode().(Attribute).getAChildNode().(Str).getText()=" | "
  // )
  // or
  // // py_3
  // (
  //   name_fixed.getId()="self"
  //   and
  //   name_fixed.getParentNode().(Attribute).getAttr()="write"
  //   and
  //   name_fixed.getParentNode().getParentNode().(Call).getAnArg().(Str).getText()="not found"
  // )
  // or
  // // py_4
  // (
  //   name_fixed.getId()="self"
  //   and
  //   name_fixed.getParentNode().(Attribute).getAttr()="write"
  //   and
  //   name_fixed.getParentNode().getParentNode().(Call).getAnArg().(Str).getText()="read error"
  //   )
  //   or
  // (
  //   // py_5
  //   name_fixed.getId()="tornado"
  //   and
  //   name_fixed.getParentNode().(Attribute).getAttr()="web"
  //   and
  //   name_fixed.getParentNode().getParentNode().(Attribute).getAttr()="HTTPError"
  //   and
  //   name_fixed.getParentNode().getParentNode().getParentNode().(Call).getArg(0).(IntegerLiteral).getN().toInt()=404
  //   and
  //   name_fixed.getParentNode().getParentNode().getParentNode().(Call).getArg(1).(Str).getText()="not found"
  // )
  // or
  // (
  //   // py_6
  //   name_fixed.getId()="unsafe_env"
  //   and
  //   name_fixed.getParentNode().(Attribute).getAttr()="get_template"
  //   and
  //   name_fixed.getParentNode().getParentNode().(Call).getAnArg().(Str).getText()="generate_new.html"
  // )
  // or
  // (
  //   // py7
  //   name_fixed.getId()="unsafe_env"
  //   and
  //   name_fixed.getParentNode().(Attribute).getAttr()="get_template"
  //   and
  //   name_fixed.getParentNode().getParentNode().(Call).getAnArg().(Str).getText()="error.html"
  // )
  // or
  // (
  //    // py_8_9_10_11
  //   name_fixed.getId()="unsafe_env"
  //   and
  //   name_fixed.getParentNode().(Attribute).getAttr()="get_template"
  //   and
  //   name_fixed.getParentNode().getParentNode().(Call).getAnArg().(Str).getText()="manage.html"
  // )
  // or
  // (
  //   // py_12
  //   name_fixed.getId()="unsafe_env"
  //   and
  //   name_fixed.getParentNode().(Attribute).getAttr()="get_template"
  //   and
  //   name_fixed.getParentNode().getParentNode().(Call).getAnArg().(Str).getText()="legal.html"
  // )
  // or
  // (
  //     // py_13
  //     name_fixed.getId()="escape"
  //     and
  //     name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Str).getText()="utf-8"
  //     and
  //     name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Call).getAChildNode().(Attribute).getAChildNode().(Call).getAChildNode().(Attribute).getAChildNode().(Name).getId()="member"
  //     and
  //     name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Call).getAChildNode().(Attribute).getAttr()="getProperty"
  //     and
  //     name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAttr()="decode"
  // )
    // or
    // (
    //   // py_14
    //   name_fixed.getId()="escape"
    //   and
    //   name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Call).getAChildNode().(Attribute).getAChildNode().(Name).getId()="group"
    //   and
    //   name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Call).getAChildNode().(Attribute).getAttr()="getProperty"
    //   and
    //   name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAttr()="decode"
    //   and
    //   name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Str).getText()="utf-8"
    // )
    // or
    // (
    // // py_15
    // name_fixed.getId()="escape"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Name).getId()="translate"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Call).getAChildNode().(Name).getId()="PMF"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Call).getArg(0).(Name).getId()="state_title"
    // )
    // or
    // (
    // // py_16
    // name_fixed.getId()="escape"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Name).getId()="user"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAttr()="getProperty"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Str).getText()="fullname"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(1).(NameConstant).getId()="None"
    // )
    // or
    // (
    //  // py_17
    // name_fixed.getId()="escape"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Name).getId()="group"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAttr()="getProperty"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Str).getText()="title"
    // and
    // name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(1).(NameConstant).getId()="None"
    // )
    // or
    // (
    //     // py_18
    //     name_fixed.getId()="escape"
    //     and
    //     name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Name).getId()="safe_unicode"
    //     and
    //     name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Name).getId()="title"
    // )
    // or
    // (
    //     // py_19_20
    //     name_fixed.getId()="Markup"
    //     and
    //     name_fixed.getParentNode().(Attribute).getAttr()="escape"
    //     and
    //     name_fixed.getParentNode().getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Attribute).getAChildNode().(Name).getId()="request"
    //     and
    //     name_fixed.getParentNode().getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Attribute).getAttr()="args"
    // //   and
    // //   name_fixed.getParentNode().getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAttr()="get"
    // //   and
    // //   name_fixed.getParentNode().getParentNode().(Call).getArg(0).(Call).getArg(0).(Str).getText()="error"
    //   )
    // or
    // (
    //   // 21
    //   name_fixed.getId()="sanitize_html"
    //   and
    //   name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Name).getId()="item"
    //   and
    //   name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAttr()="get"
    //   and
    //   name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Str).getText()="displayName"
    //   and
    //   name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(1).(Str).getText()=""
    // )
      // or
      // (
      //   //py_22_23_24
      //   name_fixed.getId()="sanitize_html"
      //   and
      //   name_fixed.getParentNode().(Call).getArg(0).(Attribute).getAChildNode().(Name).getId()="self"
      //   and
      //   (
      //     name_fixed.getParentNode().(Call).getArg(0).(Attribute).getAttr()="display_name"
      //     or
      //     name_fixed.getParentNode().(Call).getArg(0).(Attribute).getAttr()="question_text"
      //   )
      //   and
      //   (
      //     name_fixed.getParentNode().getParentNode().(KeyValuePair).getKey().(Str).getText()="display_name"
      //     or
      //     name_fixed.getParentNode().getParentNode().(KeyValuePair).getKey().(Str).getText()="display_title"
      //     or
      //     name_fixed.getParentNode().getParentNode().(KeyValuePair).getKey().(Str).getText()="problem_text"
      //   )  

      // )
      // or
      // (
      //   // 25
      //   name_fixed.getId()="sanitize_html"
      //   and
      //   name_fixed.getParentNode().(Call).getArg(0).(Name).getId()="explanation"
      //   and
      //   name_fixed.getParentNode().(Call).getParentNode().(AssignStmt).getAChildNode().(Subscript).getObject().toString()="answer"
      //   and
      //   name_fixed.getParentNode().(Call).getParentNode().(AssignStmt).getAChildNode().(Subscript).getAChildNode().(Str).getText()="explanation"
      // )
      // or
      // (
      //    // 26
      //   name_fixed.getId()="sanitize_html"
      //   and
      //   name_fixed.getParentNode().(Call).getArg(0).(Attribute).getAttr()="message"
      //   and
      //   name_fixed.getParentNode().(Call).getArg(0).(Attribute).getAChildNode().(Name).getId()="msg"
      //   and
      //   name_fixed.getParentNode().(Call).getParentNode().(KeyValuePair).getKey().(Str).getText()="message"
      // )
      // or
      // (
      //     // 27
      //     name_fixed.getId()="zone"
      //     and
      //     name_fixed.getParentNode().(For).getAChildNode().(Call).getAChildNode().(Attribute).getAChildNode().(Attribute).getAChildNode().(Name).getId()="self"
      //     and
      //     name_fixed.getParentNode().(For).getAChildNode().(Call).getAChildNode().(Attribute).getAChildNode().(Attribute).getAttr()="data"
      //     and
      //     name_fixed.getParentNode().(For).getAChildNode().(Call).getArg(0).(Str).getText()="zones"
      //     and
      //     name_fixed.getParentNode().(For).getAChildNode().(Call).getArg(1) instanceof List
      // )
      // or
      // (
      //   // py_28
      //   name_fixed.getId()="bleach"
      //   and
      //   name_fixed.getParentNode().(Attribute).getAttr()="Cleaner"
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getParentNode().(AssignStmt).getAChildNode().(Name).getId()="cleaner"
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getKeyword(0).getArg()="tags"
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getKeyword(1).getArg()="strip"
      // )
      // or
      // (
      //   // py_29
      //     (name_fixed.getId()="old_value" or name_fixed.getId()="new_value")
      //     and
      //     name_fixed.getParentNode().(Call).getAChildNode().(Name).getId()="bleach_input"
      //     and
      //     (
      //       name_fixed.getParentNode().(Call).getParentNode().(AssignStmt).getAChildNode().(Name).getId()="old_value"
      //       or
      //       name_fixed.getParentNode().(Call).getParentNode().(AssignStmt).getAChildNode().(Name).getId()="new_value"
      //     )
      // )
      // or
      // (
      //   // py_30
      //   name_fixed.getId()="select_autoescape"
      //   and
      //   name_fixed.getParentNode().(Call).getParentNode().(Keyword).getParentNode().(Call).getAChildNode().(Name).getId()="Environment"
      // )
      // or
      // (
      //   // py_31
      //   name_fixed.getId()="host"
      //   and
      //   name_fixed.getParentNode().getAChildNode().(Name).getId()="repr"
      //   and
      //   name_fixed.getParentNode().(Call).getParentNode().(BinaryExpr).getAChildNode().(Str).getText()="host %s not in vhost map"
      //   and
      //   name_fixed.getParentNode().(Call).getParentNode().(BinaryExpr).getParentNode().(Call).getAChildNode().(Attribute).getAttr()="NoResource"
      // )
      // or
      // (
      //   // py_32_33
      //   name_fixed.getId()="_UnsafeErrorPage"
      //   and
      //   name_fixed.getParentNode().(Call).getArg(0).(IntegerLiteral).getN().toInt()=500
      //   and
      //   name_fixed.getParentNode().(Call).getArg(1).(Str).getText()="Internal Error"
      //   and
      //   name_fixed.getParentNode().(Call).getArg(2).(Str).getText()=""
      // )
      // or
      // (
      //     // 34
      //     name_fixed.getId()="resource"
      //     and
      //     name_fixed.getParentNode().(Attribute).getAttr()="_UnsafeErrorPage"
      //     and
      //     name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(0).(Attribute).getAttr()="INTERNAL_SERVER_ERROR"
      //     and
      //     name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(0).(Attribute).getAChildNode().(Name).getId()="http"
      //     and
      //     name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(1).(Str).getText()="Server Connection Lost"
      //     )
      //   or
      // (
      //   // py_35_39_45
      //   name_fixed.getId()="resource"
      //   and
      //   name_fixed.getParentNode().(Attribute).getAttr()="_UnsafeNoResource"
      //   and
      //   name_fixed.getParentNode().getParentNode() instanceof Call
      //   and
      //   name_fixed.getParentNode().getParentNode().getParentNode() instanceof Return
      // )
      // or
      // (
      //     // 36
      //     name_fixed.getId()="_UnsafeNoResource"
      //     and
      //     name_fixed.getParentNode().getParentNode() instanceof Return
      //     and
      //     name_fixed.getParentNode().getScope().getBody().getItem(0) instanceof ExprStmt
      // )
      // or
      // (
      //   // 37
      //   name_fixed.getId()="_UnsafeErrorPage"
      //   and
      //   name_fixed.getParentNode().(Attribute).getAttr()="__init__"
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getArg(0).(Name).getId()="self"
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getArg(1).(Name).getId()="NOT_FOUND"
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getArg(2).(Str).getText()="No Such Resource"
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getArg(3).(Name).getId()="message"
      //   )
      // or
      // (
      //   // 38
      //   name_fixed.getId()="resource"
      //   and
      //   name_fixed.getParentNode().(Attribute).getAttr()="_UnsafeErrorPage"
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getArg(0).(IntegerLiteral).getN().toInt()=500
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getArg(1).(Str).getText()="Whoops! Internal Error"
      // )
      // or
      // (
      //   // 40
      //   name_fixed.getId()="resource"
      //   and
      //   name_fixed.getParentNode().(Attribute).getAttr()="_UnsafeNoResource"
      //   and
      //   name_fixed.getParentNode().getParentNode().getParentNode().(Attribute).getAttr()="render"
      //   and
      //   name_fixed.getParentNode().getParentNode().getParentNode().getParentNode().(Call).getAnArg().(Name).getId()="request"
      //   and
      //   name_fixed.getParentNode().getParentNode().getParentNode().getParentNode().getParentNode() instanceof Return
      //   )
      // or
      // (
      //   // 41
      //   name_fixed.getId()="resource"
      //   and
      //   name_fixed.getParentNode().(Attribute).getAttr()="_UnsafeNoResource"
      //   and
      //   name_fixed.getParentNode().getParentNode().getParentNode().(Attribute).getAttr()="render"
      //   and
      //   name_fixed.getParentNode().getParentNode().getParentNode().getParentNode().(Call).getAnArg().(Name).getId()="request"
      //   and
      //   name_fixed.getParentNode().getParentNode().(Call).getArg(0).(Str).getText()="File not found."
      // )
      // or
        // (
        //   // py_42_43_44
        //   name_fixed.getId()="resource"
        //   and
        //   name_fixed.getParentNode().(Attribute).getAttr()="_UnsafeErrorPage"
        //   and
        //   name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(0).(Attribute).getAttr()="INTERNAL_SERVER_ERROR"
        //   and
        //   name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(0).(Attribute).getAChildNode().(Name).getId()="http"
        //   and
        //   name_fixed.getParentNode().(Attribute).getParentNode().(Call).getArg(1).(Str).getText()="Request did not return bytes"
        // )
        // or
        // (
        //   // 45
        //   name_fixed.getId()="resource"
        //   and
        //   name_fixed.getParentNode().(Attribute).getAttr()="_UnsafeNoResource"
        //   and
        //   name_fixed.getParentNode().getParentNode().getParentNode() instanceof Return
        // )
        // or
        // (
        //   // 46_47
        //   name_fixed.getId()="clean_html"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Name).getId()="html"
        //   and
        //   name_fixed.getParentNode().getParentNode().(AssignStmt).getAChildNode().(Name).getId()="html"
        // )
        // or
        // (
        //       // 48
        //       name_fixed.getId()="Markup"
        //       and
        //      (
        //       name_fixed.getParentNode().(Call).getArg(0).(Call).getAKeyword().getArg().toString()="beancount_version"
        //       or
        //       name_fixed.getParentNode().(Call).getArg(0).(Call).getAKeyword().getArg().toString()= "fava_version"
        //      ) 
        //      and
        //      name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Name).getId()="html"
        //      and
        //      name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Name).getId()="render_template_string"
        // )
        // or
        // (
        //   // 49
        //   name_fixed.getId()="Markup"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(BinaryExpr).getLeft().(Subscript).getAChildNode().(Call).getAChildNode().(Name).getId()="entry"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(BinaryExpr).getLeft().(Subscript).getAChildNode().(Call).getAChildNode().(Name).getId()="get_entry_slice"
        // )
        // or
        // (
          // 50
        //     name_fixed.getId()="Markup"
        //     and
        //     name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Name).getId()="entry"
        //     and
        //     name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(2).(Name).getId()="indent"
        //     and
        //     name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(1).(Attribute).getAChildNode().(Attribute).getAChildNode().(Attribute).getAChildNode().(Name).getId()="self"
        //     and
        //     name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(1).(Attribute).getAChildNode().(Attribute).getAChildNode().(Attribute).getAttr()="ledger"
        //     and
        //     name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(1).(Attribute).getAChildNode().(Attribute).getAttr()="fava_options"
        //     and
        //     name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(1).(Attribute).getAttr()="currency_column"
        // )
        // or
        // (
        //   // 51
        //   name_fixed.getId()="Markup"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Name).getId()="message"
        //   and
        //   name_fixed.getParentNode().getParentNode() instanceof Return
        // )
        // or
        // (
        //   // 52
        //   name_fixed.getId()="Markup"
        //   and
        //   name_fixed.getParentNode().getParentNode() instanceof Return
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAttr()="replace"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Call).getAChildNode().(Attribute).getAttr()="replace"
        // )
        // or
        // (
        //   // 53_54
        //   name_fixed.getId()="clean"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Name).getId()="value"
        //   and
        //   name_fixed.getParentNode().getParentNode() instanceof Return
        // )
        // or
        // (
        //   // 55
        //   name_fixed.getId()="sanitizer"
        //   and
        //   name_fixed.getParentNode().(Attribute).getAttr()="clean"
        //   and
        //   name_fixed.getParentNode().getParentNode().(Call).getArg(0).(Name).getId()="content"
        //   and
        //   name_fixed.getParentNode().getParentNode().getParentNode() instanceof Return
        // )
        // or
        // (
        //   // 56
        //   name_fixed.getId()="sanitize_callback"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAChildNode().(Name).getId()="self"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Call).getAChildNode().(Attribute).getAttr()="get_argument"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Call).getArg(0).(Str).getText()="callback"
        //   )
        //   or
        // 57_removed
        // (
        //   // 58
        //   name_fixed.getId()="escape"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Attribute).getAChildNode().(Attribute).getAChildNode().(Name).getId()="unit"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Attribute).getAChildNode().(Attribute).getAttr()="translation"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Attribute).getAttr()="language"
        // )
        // or
        // (
        //   // 59
        //   name_fixed.getId()="escape"
        //   and
        //   name_fixed.getParentNode().(Call).getParentNode().(Call).getAChildNode().(Attribute).getAChildNode().(Name).getId()="language_format"
        //   and
        //   name_fixed.getParentNode().(Call).getParentNode().(Call).getAChildNode().(Attribute).getAttr()="format"
        //   )
        //   or
        // (
          // 60
        //   name_fixed.getId()="escape"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Subscript).getAChildNode().(Name).getId()="t"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Subscript).getAChildNode().(IntegerLiteral).getN().toString()="0"
        //   and
        //   name_fixed.getParentNode().getParentNode().(Call).getArg(1).getAChildNode().(Name).getId()="escape"
        //   and
        //   name_fixed.getParentNode().getParentNode().(Call).getArg(1).(Call).getArg(0).(Subscript).getAChildNode().(Name).getId()="t"
        // )
        // or
        // (
        //   // 61
        //   name_fixed.getId()="escape"
        //   and
        //   name_fixed.getParentNode().(Call).getArg(0).(Subscript).getAChildNode().(Name).getId()="item"
        //   and
        //   (
        //     name_fixed.getParentNode().(Call).getArg(0).(Subscript).getAChildNode().(Str).getText()="name"
        //     or
        //     name_fixed.getParentNode().(Call).getArg(0).(Subscript).getAChildNode().(Str).getText()="email"
        //   )
        //   and
        //   name_fixed.getParentNode().getParentNode().getParentNode().getAChildNode().(Attribute).getAttr()="format"
        //   and
        //   name_fixed.getParentNode().getParentNode().getParentNode().getAChildNode().(Attribute).getAChildNode().(Name).getId()="cell_name"
        // )
        // or
        // (
        //   // 62
        //   name_fixed.getId()="ast"
        //   and
        //   name_fixed.getParentNode().(Attribute).getAttr()="literal_eval"
        //   and
        //   name_fixed.getParentNode().getParentNode().(Call).getArg(0).(Call).getAChildNode().(Name).getId()="str"
        //   and
        //   name_fixed.getParentNode().getParentNode().getParentNode() instanceof AssignStmt
        //   and
        //   name_fixed.getParentNode().getParentNode().getParentNode().getAChildNode().(Name).getId()="status"
        // )
        // or
        (
          // 63
          name_fixed.getId()="escape"
          and
          name_fixed.getParentNode().(Call).getArg(0).(Dict).getAChildNode().(KeyValuePair).getKey().(Str).getText()="entry"
          and
          name_fixed.getParentNode().(Call).getArg(0).(Dict).getAChildNode().(KeyValuePair).getValue().(Name).getId()="file_db_entry"
        )

}

from Name name_fixed, Stmt stmt
where 
isFixed(name_fixed)
select name_fixed, name_fixed.getLocation()," The file is correctly fixed"


