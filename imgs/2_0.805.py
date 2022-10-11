d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.W, Length.medium)
d.position_pen(0,1)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.position_pen(3,0)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.S, Length.short)

d.end()
