d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)

d.end()
