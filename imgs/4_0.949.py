d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)

d.end()
