d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,1)

d.end()
