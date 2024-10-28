from functools import reduce

class HTMLNode:
    def __init__(self, tag = None, value = None, children  = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ''
       
        return "".join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value is None:
            raise ValueError("No value provided.")
        if self.tag is None or self.tag == "":
            return self.value
        
        all_props = self.props_to_html()

        return f"<{self.tag}{all_props}>{self.value}</{self.tag}>"
    

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided.")
        if self.children is None:
            raise ValueError("No children provided.")
        
        all_children = ""

        for child in self.children:
            all_children += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{all_children}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

