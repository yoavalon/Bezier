d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.short, Radius.low)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.long)

d.end()
