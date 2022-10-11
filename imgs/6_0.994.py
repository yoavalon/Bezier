d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(3,1)
d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.long)

d.end()
