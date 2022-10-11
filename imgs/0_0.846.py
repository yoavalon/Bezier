d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.short)

d.end()
