d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
