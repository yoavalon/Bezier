d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)

d.end()
