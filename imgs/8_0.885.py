d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.N, Length.long)
d.position_pen(0,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.position_pen(0,3)

d.end()
