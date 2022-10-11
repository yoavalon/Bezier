d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)

d.end()
