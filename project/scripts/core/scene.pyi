class Scene_Base:
    """
    场景基类。
    
    该类提供了场景对象的基本属性和方法。
    
    属性:
    
        __quitted: 退出标志。
        
    方法:
    
        load_data_from_json(file): 从JSON文件中加载数据。
        update(): 更新方法。
        quit(): 退出方法。
    """
    
    __quitted: bool
    """退出标志"""
    
    def __init__(self) -> None:
        """
        初始化场景对象。

        根据场景对象的属性，将窗口、表面和精灵添加到Graphics模块中。
        """
        pass
                
    def load_data_from_json(self, file: str) -> None:
        """
        从JSON文件中加载数据，解析成为对应Python代码。
        
        参数:
        
            file: JSON文件路径。
        """
        pass

    def update(self) -> None:
        """基类的更新仅仅是更新Graphics模块。"""
        pass
        
    def quit(self) -> None:
        """退出场景。此时将冻结Graphics模块，并释放所有资源。"""
        pass
    
    def __del__(self) -> None:
        """析构函数。用以防范场景对象未被正确释放的情况。"""
        pass